class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)

        i, j = 0, len(people) - 1
        boats = 0
        print(people)
        while i <= j:
            total_weight = people[i] + people[j]
            boats += 1
            if total_weight <= limit:
                i += 1
                j -= 1
                continue

            elif total_weight < limit:
                i += 1
                continue

            else:
                j -= 1

        return boats

             
        