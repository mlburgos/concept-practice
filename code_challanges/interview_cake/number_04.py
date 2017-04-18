# Write a function merge_ranges() that takes a list of meeting time ranges and
# returns a list of condensed ranges.
#
# given: [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# return: [(0, 1), (3, 8), (9, 12)]


def merge_ranges(time_slots):
    combined_slots = [time_slots[0]]

    for i, time_slot in enumerate(time_slots):
        if i == 0:
            continue

        print 'time_slot:', time_slot

        time_slot_start = time_slot[0]
        time_slot_end = time_slot[1]

        for i, slot in enumerate(combined_slots):
            print 'slot:', slot
            slot_start = slot[0]
            slot_end = slot[1]

            if time_slot_start >= slot_start and time_slot_end <= slot_end:
                break
            if time_slot_start <= slot_start and time_slot_end >= slot_end:
                combined_slots[i] = time_slot
            elif time_slot_start <= slot_start and time_slot_end >= slot_start:
                combined_slots[i] = (time_slot_start, slot_end)
            elif time_slot_end >= slot_end and time_slot_start <= slot_end:
                combined_slots[i] = (slot_start, time_slot_end)
            else:
                combined_slots.append(time_slot)

    return combined_slots



##########################################################################################
# Baby steps

test = [(1, 3), (2, 4)]
# return: [(1, 4)]
def test_run(test):
    time1_start = test[0][0]
    time1_end = test[0][1]

    time2_start = test[1][0]
    time2_end = test[1][1]

    result = []
    new_start = 0
    new_end = 0


    if time1_start <= time2_start and time1_end >= time2_start:
        new_start = time1_start
    elif time2_start <= time1_start and time2_end >= time1_start:
        new_start = time2_start

    if time1_end >= time2_end and time1_start <= time2_end:
        new_end = time1_end
    elif time2_end >= time1_end and time2_start <= time1_end:
        new_end = time2_end

    return


##########################################################################################
# My solution

def merge_ranges(time_slots):
    time_slots.sort()

    merged_ranges = []

    a_time = time_slots[0]
    b_time = time_slots[1]

    time_slots_remain = True

    i = 1

    while time_slots_remain:
        print i
        print 'a_time:', a_time
        print 'b_time:', b_time

        # check if they overlap
        if a_time[1] >= b_time[0] and b_time[1] >= a_time[1]:
            a_time = (a_time[0], b_time[1])

            if i < len(time_slots) - 1:
                b_time = time_slots[i + 1]
            else:
                merged_ranges.append(a_time)
                time_slots_remain = False
        # check if the second is spanned entirely by the first
        elif a_time[0] <= b_time[0] and a_time[1] >= b_time[1]:
            if i < len(time_slots) - 1:
                b_time = time_slots[i + 1]
            else:
                merged_ranges.append(a_time)
                time_slots_remain = False
        # no overlap at all
        else:
            merged_ranges.append(a_time)
            if i < len(time_slots) - 1:
                a_time = time_slots[i]
                b_time = time_slots[i + 1]
            else:
                merged_ranges.append(time_slots[i])
                time_slots_remain = False
        i += 1

    return merged_ranges

##########################################################################################
# Their solution from mem


def merged_ranges(time_slots):

    time_slots.sort()

    merged_ranges = [time_slots[0]]

    for current_start, current_end in time_slots[1:]:

        # *** good trip for tuples *** good for clean code
        last_merged_meeting_start, last_merged_meeting_end = merged_ranges[-1]

        if last_merged_meeting_end >= current_start:
            merged_ranges[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_end))

        else:
            merged_ranges.append((current_start, current_end))

    return merged_ranges
