
# finds free slots that match in two people's calendars
def schedule(p1_cal, p1_bounds, p2_cal, p2_bounds, meeting_length):
    final_result = []

    # add in fake time slots based on the bounds
    p1_cal.insert(0, [p1_bounds[0], p1_bounds[0]])
    p1_cal.append([p1_bounds[1], p1_bounds[1]])

    p2_cal.insert(0, [p2_bounds[0], p2_bounds[0]])
    p2_cal.append([p2_bounds[1], p2_bounds[1]])

    # get free slots
    nums_and_letters1 = get_free_slots(p1_cal, meeting_length)
    p1_free_slots_num = nums_and_letters1[0]
    p1_free_slots_let = nums_and_letters1[1]

    nums_and_letters2 = get_free_slots(p2_cal, meeting_length)
    p2_free_slots_num = nums_and_letters2[0]
    p2_free_slots_let = nums_and_letters2[1]

    for i in range(len(p1_free_slots_num)):
        result = []
        s1 = p1_free_slots_num[i][0]
        e1 = p1_free_slots_num[i][1]
        s2 = p2_free_slots_num[i][0]
        e2 = p2_free_slots_num[i][1]

        if s2 >= s1:
            if e2 >= e1:
                result.append(p2_free_slots_let[i][0])
                result.append(p1_free_slots_let[i][1])
            else:
                result.append(p2_free_slots_let[i][0])
                result.append(p2_free_slots_let[i][1])
        else:
            if e2 >= e1:
                result.append(p1_free_slots_let[i][0])
                result.append(p1_free_slots_let[i][1])
            else:
                result.append(p1_free_slots_let[i][0])
                result.append(p2_free_slots_let[i][1])

        final_result.append(result)

    # print free slots
    print("#1")
    print(p1_cal)
    print(p1_bounds)
    print("\n#2")
    print(p2_cal)
    print(p2_bounds)
    print("\nFree slots found for #1: " + str(p1_free_slots_let))
    print("Free slots found for #2: " + str(p2_free_slots_let))
    print("\nTimes that both are free: " + str(final_result))

# finds free slots in a calendar
def get_free_slots(p_cal, meeting_length):
    p_free_slots_nums = []
    p_free_slots_lets = []

    for i in range(len(p_cal)-1):
        start = p_cal[i][1]
        end = p_cal[i+1][0]

        # check if meeting length can fit in available slot
        # convert string to minutes
        start_minutes = convert_time_string_to_minutes(start)
        end_minutes = convert_time_string_to_minutes(end)

        if (end_minutes - start_minutes) >= meeting_length:
            p_free_slot_num = [start_minutes, end_minutes]
            p_free_slots_let = [start, end]

            p_free_slots_nums.append(p_free_slot_num)
            p_free_slots_lets.append(p_free_slots_let)

    return [p_free_slots_nums, p_free_slots_lets]

# converts 4 or 5 length time string to minutes
def convert_time_string_to_minutes(time_string):
    if len(time_string) == 5:
        minutes = ((int(time_string[0]) * 600) +
                   (int(time_string[1]) * 60) +
                   (int(time_string[3]) * 10) +
                   (int(time_string[4]) * 1))
    else:
        minutes = ((int(time_string[0]) * 60) +
                   (int(time_string[2]) * 10) +
                   (int(time_string[3]) * 1))
    return minutes

# main function for sending calendars and meeting length
def main():
    schedule([['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']],
             ['9:00', '20:00'],
             [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']],
             ['10:00', '18:30'], 30)

if __name__ == "__main__":
    main()
