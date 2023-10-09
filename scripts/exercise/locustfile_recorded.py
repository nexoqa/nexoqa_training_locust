from locust import task, run_single_user
from locust import FastHttpUser


class localhost(FastHttpUser):
    host = "http://localhost:8080"
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "es,es-419;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Cache-Control": "no-cache",
                "Cookie": "jenkins-timestamper-offset=-7200000; screenResolution=1680x1050; JSESSIONID.97af832c=node01bvsfy69a79ta1qj8ky5w2ctl83.node0; JSESSIONID.ebb06f37=node017oiopx5extgg11e45vbp033h45.node0",
                "Host": "localhost:8080",
                "Pragma": "no-cache",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/songs",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer null",
                "Cache-Control": "no-cache",
                "Host": "localhost:8081",
                "Origin": "http://localhost:8080",
                "Pragma": "no-cache",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "Cache-Control": "no-cache",
                "Cookie": "jenkins-timestamper-offset=-7200000; screenResolution=1680x1050; JSESSIONID.97af832c=node01bvsfy69a79ta1qj8ky5w2ctl83.node0; JSESSIONID.ebb06f37=node017oiopx5extgg11e45vbp033h45.node0",
                "Host": "localhost:8080",
                "Pragma": "no-cache",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "POST",
            "http://localhost:8081/register",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer null",
                "Content-Length": "52",
                "Host": "localhost:8081",
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
            json={"email": "user3@vtech.com", "password": "12312312312"},
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/songs",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "If-None-Match": 'W/"6be-oh0TqHk9gczAX3+xI1r3xp1wiAU"',
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/bookmarks",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "If-None-Match": 'W/"2-l9Fw4VUO7kr8CvBlt4zaMCqXZ0w"',
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/histories",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "If-None-Match": 'W/"2-l9Fw4VUO7kr8CvBlt4zaMCqXZ0w"',
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/songs?search=N",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/songs?search=Ne",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/songs?search=Nev",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/songs?search=Neve",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/songs?search=Never",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/songs/1",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "If-None-Match": 'W/"14f-LKSD+VROcp6fpVz5Th+pB2Jui2E"',
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/songs/1",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "If-None-Match": 'W/"143-VPiG4O4ntO9Worzqqu2k07I5LpQ"',
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "http://localhost:8081/histories",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Content-Length": "12",
                "Host": "localhost:8081",
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
            json={"songId": 1},
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/bookmarks?songId=1",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "If-None-Match": 'W/"2-l9Fw4VUO7kr8CvBlt4zaMCqXZ0w"',
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "http://localhost:8081/bookmarks",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Content-Length": "12",
                "Host": "localhost:8081",
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
            json={"songId": 1},
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/songs",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "If-None-Match": 'W/"6be-oh0TqHk9gczAX3+xI1r3xp1wiAU"',
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/bookmarks",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/histories",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/songs/2",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/songs/2",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "If-None-Match": 'W/"14a-C4oekYpMgKC7FZ7aMoWVeVReniM"',
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "http://localhost:8081/histories",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Content-Length": "12",
                "Host": "localhost:8081",
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
            json={"songId": 2},
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/bookmarks?songId=2",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/songs",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "If-None-Match": 'W/"6be-oh0TqHk9gczAX3+xI1r3xp1wiAU"',
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/bookmarks",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "If-None-Match": 'W/"2a6-EvQK5VXV/FJsfIogytZXzmnsFbw"',
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "http://localhost:8081/histories",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyM0B2dGVjaC5jb20iLCJwYXNzd29yZCI6IiQyYSQwOCRsS0dzZGJJYi5UeW5kZ2FhRFAvOVp1SkRQSjRxT3JzbWlwazhvTHZRS1lxM2lSRUR2Um9jVyIsInVwZGF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImNyZWF0ZWRBdCI6IjIwMjMtMTAtMDlUMTY6MDA6MjEuMTQ0WiIsImlhdCI6MTY5Njg2NzIyMSwiZXhwIjoxNjk3NDcyMDIxfQ.tqNPUjAYBtzXJgzUWmo8UoBXiGglx8kLvpwLlabTE98",
                "Host": "localhost:8081",
                "Origin": "http://localhost:8080",
                "Referer": "http://localhost:8080/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(localhost)
