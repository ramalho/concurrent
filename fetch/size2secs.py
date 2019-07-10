#!/usr/bin/env python3


'''

Download times from office rated at ~110 Mbps by Fast.com

15
      35_571 B   0.712 s          49_981 B/s
      32_139 B   0.654 s          49_166 B/s
      35_607 B   0.657 s          54_222 B/s
16
      85_181 B   0.833 s         102_244 B/s
      71_001 B   0.869 s          81_718 B/s
      91_966 B   0.826 s         111_303 B/s
17
     108_033 B   0.932 s         115_884 B/s
     183_336 B   1.095 s         167_401 B/s
     142_520 B   0.912 s         156_246 B/s
18
     364_729 B   1.250 s         291_824 B/s
     234_966 B   1.094 s         214_683 B/s
     337_301 B   1.326 s         254_290 B/s
19
     418_524 B   1.103 s         379_503 B/s
     418_020 B   1.141 s         366_358 B/s
     663_463 B   1.327 s         499_885 B/s
20
   1_015_045 B   1.402 s         724_020 B/s
   1_006_040 B   1.482 s         678_818 B/s
   1_050_085 B   1.581 s         664_217 B/s
21
   2_660_339 B   1.792 s       1_484_568 B/s
   2_004_828 B   1.632 s       1_228_609 B/s
   2_359_048 B   1.496 s       1_576_948 B/s
22
   4_929_829 B   1.670 s       2_951_827 B/s
   3_024_820 B   1.527 s       1_981_132 B/s
   4_689_225 B   1.738 s       2_697_399 B/s
23
   6_308_178 B   1.908 s       3_305_505 B/s
   6_516_131 B   2.061 s       3_161_128 B/s
   8_799_420 B   2.190 s       4_018_563 B/s
24
  22_219_334 B   4.949 s       4_489_783 B/s
  20_222_864 B   5.954 s       3_396_599 B/s
  13_513_327 B   2.289 s       5_902_841 B/s
25
  27_409_511 B   4.000 s       6_852_956 B/s
  24_224_693 B   3.650 s       6_637_281 B/s
  29_403_262 B   3.841 s       7_654_395 B/s
26
  47_976_955 B   6.057 s       7_920_590 B/s
  62_296_842 B   6.607 s       9_428_602 B/s
  77_726_028 B   7.575 s      10_260_385 B/s
27
 101_284_112 B   9.320 s      10_867_530 B/s
 103_284_185 B  12.984 s       7_954_780 B/s
 100_805_313 B   9.850 s      10_234_147 B/s
28
 226_102_411 B  24.221 s       9_334_924 B/s
 233_682_756 B  20.046 s      11_657_228 B/s
 215_064_763 B  20.734 s      10_372_524 B/s

    #bps = size / dt
    #print(f'{size:12_d} B\t{dt:7.3f} s\t{bps:11_.0f} B/s')

'''

import collections
import math
from urllib import request
from urllib import parse
import pathlib
import time
import random
from concurrent import futures


BASE_URL = 'https://upload.wikimedia.org/wikipedia/commons/'
LOCAL_PATH = 'img/'
SAMPLE_LEN = 3

PathSize = collections.namedtuple('PathSize', 'path size')
TimeSize = collections.namedtuple('TimeSize', 'time size')

def group_by_size():
    jpeg_by_size = collections.defaultdict(list)
    with open('urls/jpeg.txt') as fp:
        for line in fp:
            size_field, path = line.strip().split()
            size = int(size_field)
            size_group = round(math.log(size, 2))
            jpeg_by_size[size_group].append(PathSize(path, size))
    return jpeg_by_size


def file_name(url):
    url_parts = parse.urlsplit(url)
    path = pathlib.PurePath(url_parts.path)
    return path.parts[-1]


def fetch(size_group, path_size: PathSize):
    url = BASE_URL + path_size.path 
    t0 = time.perf_counter()
    with request.urlopen(url) as req:
        assert req.status == 200
        octets = req.read()
        assert len(octets) == path_size.size
    dt = time.perf_counter() - t0

    name = file_name(url)
    save_path = LOCAL_PATH + name 
    with open(save_path, 'wb') as fp:
        fp.write(octets)

    return (size_group, dt, len(octets), name)


def fetch_group(size_group, path_list, executor):
    random.shuffle(path_list)
    sample = path_list[:SAMPLE_LEN]
    future_map = {}
    for path_size in sample:
        future_map[executor.submit(fetch, size_group, path_size)] = path_size
    return future_map


def main():
    jpeg_by_size = group_by_size()
    with futures.ThreadPoolExecutor() as executor:

        # submit tasks
        future_map = {}
        for size_group in jpeg_by_size:
            group_map = fetch_group(size_group, jpeg_by_size[size_group], executor)
            future_map.update(group_map)

        # get results
        group_times = collections.defaultdict(list)
        for future in futures.as_completed(future_map):
            path_size = future_map[future]
            size_group, dt, size, name = future.result()
            group = group_times[size_group]
            group.append(TimeSize(dt, size))
            if len(group) == SAMPLE_LEN:
                times, sizes = [sum(x) for x in zip(*group)]
                avg_time = times / SAMPLE_LEN
                avg_size = sizes / SAMPLE_LEN
                print(f'Group {size_group} _____________ total _______ average')
                print(f' size   \t{sizes:12_d} B\t{avg_size:12_.0f} B')
                print(f' time   \t{times:12_.2f} s\t{avg_time:12_.2f} s')
                print(f' rate   \t\t\t{sizes/times:12_.0f} B/s')


if __name__ == '__main__':
    main()
