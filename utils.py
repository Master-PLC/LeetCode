#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :utils.py
@Description  :
@Date         :2021/12/20 20:13:50
@Author       :Arctic Little Pig
@version      :1.0
'''

import copy
import time


class UniTest(object):
    def __init__(self) -> None:
        super(UniTest, self).__init__()
        self.unequal_sample = 0
        self.unequal_list = []
        self.num_test = 1000
        self.time_count = 0

    def reInit(self):
        self.unequal_sample = 0
        self.unequal_list = []

    def uniTest(self, testFunc, test_data, equalFunc=None):
        self.reInit()
        print(f"---> {self.num_test} test of {len(test_data)} samples")

        data_size = len(test_data)
        for _ in range(self.num_test):
            for i, data in enumerate(copy.deepcopy(test_data)):
                rtn = data.pop("rtn")
                time_start = time.clock()
                res = testFunc(**data)
                elapsed = (time.clock() - time_start) * 1000
                self.time_count += elapsed
                self.assertEqual(i, res, rtn, equalFunc)

        if self.unequal_sample == 0:
            print("Congratulations! All the samples passed the test!")
        else:
            print(
                f"Following sample index didn't pass the test: {self.unequal_list}")
        print(
            f"Mean test time of one sample: {self.time_count / (self.num_test * data_size):4.3f}ms")

    def assertEqual(self, idx, result, expected_result, equalFunc=None):
        try:
            if not equalFunc:
                assert result == expected_result
            else:
                assert equalFunc(result, expected_result)
            # print(
            #     f"Sample ID: {idx} --- Function return matches the expected result.")
        except Exception:
            if idx not in self.unequal_list:
                self.unequal_sample += 1
                self.unequal_list.append(idx)
                print(
                    f"Sample ID: {idx} --- Function return-'{result}' doesn't match the expected result-'{expected_result}'.")


tester = UniTest()

__all__ = (tester, )
