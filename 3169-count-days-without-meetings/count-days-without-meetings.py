class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available_days, last_end_day = 0, 0

        for start_day, end_day in meetings:
            if end_day > days:
                break

            if start_day > last_end_day:
                available_days += start_day - (last_end_day + 1)
                last_end_day = end_day
            
            last_end_day = max(last_end_day, end_day)
        
        if last_end_day < days:
            available_days += days - last_end_day

        return available_days