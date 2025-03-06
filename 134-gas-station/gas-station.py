from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_gas, cost_until, cost_after, gas_until, gas_after, start_index = 0, 0, 0, 0, 0, 0

        for i in range(len(gas)):
            g = gas[i]
            c = cost[i]

            cur_gas += g - c
            cost_after += c
            gas_after += g

            if cur_gas < 0:
                start_index = i + 1
                cur_gas = 0
                gas_until += gas_after
                cost_until += cost_after
                gas_after = 0
                cost_after = 0

        if start_index < len(gas):
            remaining = (cur_gas + gas_until) - cost_until
            if remaining >= 0:
                return start_index

        return -1