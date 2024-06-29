def getBooking_number(booking_slot):
    interval = booking_slot.split(' ')
    if len(interval) == 1:
        return ([None, int(interval[0])])

    return [int(interval[0]), int(interval[1])]


def isCancel(booking):
    return booking[0] is None


def book_slot(slots, start, end, available_slot, total_visits):
    # check for island booking
    # if start == 0 and slots.get(end + 1, 0) == 0:
    #     total_visits += 1
    # elif end == 35 and slots.get(start - 1, 0) == 0:
    #     total_visits += 1
    # elif slots.get(start - 1, 0) == 0 and slots.get(end + 1, 0) == 0:
    #     total_visits += 1

    for i in range(start, end + 1):
        if slots.get(i, 0) == 0:
            available_slot -= 1

        slots[i] = slots.get(i, 0) + 1

        # if (start != 0 or end != 35) and slots.get(i, 0) == 1:
        #     total_visits -= 1

    return total_visits, available_slot


def cancel_book(slots, start, end, available_slot, total_visits):
    time_gaps = 0
    ready_to_take_gap = True
    for i in range(start, end + 1):
        slots[i] = slots.get(i, 0) - 1

        if slots.get(i, 0) == 0:
            available_slot += 1

    # print('GAP:   ', time_gaps, start, end)

    return total_visits, available_slot


def get_visit_times(slots):
    sequence_count = 0
    count = 0
    for n in range(36):
        if slots.get(n, 0) > 0:

            if sequence_count >= 0:
                count += 1
                sequence_count = -1
            else:
                sequence_count = -1
        else:
            sequence_count += 1

    return (count)
