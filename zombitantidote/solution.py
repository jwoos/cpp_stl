def answer(meetings):
    sorted_meetings = sorted(meetings, key=lambda meeting: meeting[1])
    meeting_lists = []
    for meeting in meetings:
      overlap = False
      for meeting_list in meeting_lists:
        if meeting[0] < meeting_list[1] and meeting[1] > meeting_list[0]:
          overlap = True
        elif meeting[1] > meeting_list[0] and meeting[0] < meeting_list[1]:
          overlap = True
      if overlap == False:
        meeting_lists.append(meeting)
    return len(meeting_lists)
