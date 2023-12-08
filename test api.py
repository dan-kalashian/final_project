import json
import requests
import re
umd_request = requests.get("https://api.umd.io/v1/courses?dept_id=ENGL")
umd_data=json.loads(umd_request.content)
print(umd_data)
for course in umd_data:
    course_id = course["course_id"]
    dept_id = course["dept_id"]
    if dept_id=='ENGL':
        print(f"{course['course_id']}: {course['name']}")
