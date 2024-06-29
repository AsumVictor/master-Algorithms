from helper import *


def main():

    def create_slot(N, avail):
        spots = {}
        slots_intervals = {}
        book_count = 0
        total_avail_slot = 36
        total_visits = 0
        for i in range(0, 36):
            spots[i] = 0

        for i in range(N):
            booking_number = getBooking_number(avail[i])

            if not isCancel(booking_number):
                book_count += 1
                slots_intervals[book_count] = (
                    booking_number[0], booking_number[1])
                total_visits, total_avail_slot = book_slot(
                    spots, booking_number[0], booking_number[1], total_avail_slot, total_visits)
            else:
                booking_number = booking_number[1] * -1
                total_visits, total_avail_slot = cancel_book(spots, slots_intervals.get(booking_number)[
                    0], slots_intervals.get(booking_number)[1], total_avail_slot, total_visits)
            
            total_visits = get_visit_times(spots)
            print(f'Visits: {total_visits}  Slots:  {total_avail_slot}')
            # print(spots)

            # print(booking_number)
        # print(spots)

    create_slot(12, ['2 2', '17 26', '-2', '12 21', '0 0', '19 21',
                '16 22', '14 20', '15 19', '13 14', '-4', '13 17'])


if __name__ == '__main__':
    main()
