
attendance=[

    {"name":"abin","attendance_count":28,"count":1},
    {"name":"aadhil","attendance_count":20,"count":2},
    {"name":"adhnan","attendance_count":20,"count":2},
    {"name":"arya","attendance_count":25,"count":5},
    {"name":"clairin","attendance_count":25,"count":4},
    {"name":"joji","attendance_count":26,"count":7},
    {"name":"libin","attendance_count":28,"count":7},
    {"name":"lijo","attendance_count":21,"count":2},
    {"name":"shajeer","attendance_count":27,"count":2},
    {"name":"shafi","attendance_count":28,"count":7},
    {"name":"resin","attendance_count":24,"count":3},
    {"name":"lakshmi","attendance_count":16,"count":6},
    {"name":"thammana","attendance_count":25,"count":1},
    {"name":"VARSHANA","attendance_count":8,"count":0},

]

srt_attendance_count =sorted(attendance,key=lambda dict:dict.get("attendance_count"))

# print(srt_attendance_count)

name_attendance = [{st.get("name"):st.get("attendance_count")} for st in srt_attendance_count]

# print(name_attendance)

srt_hacker_rank_count = sorted(attendance,key=lambda dict:dict.get("count"))

# print(srt_hacker_rank_count)

name_hacker_rank_count =[{st.get("name"):st.get("count")} for st in srt_hacker_rank_count]

print(name_hacker_rank_count)

