<template>
  <div class="container col-md-10 pt-5">
    <div class="profile">
        <div class="card p-3">
          <div class="d-flex">
            <div>
              <span class="my-auto ml-3" style="color:pink; font-size:3rem; font-weight:bold;">{{profileData.username}}</span>
              <span class="ml-2" style="font-size:1.5rem; font-weight:bold; ">님의 프로필</span>
            </div>
            <div class="ml-auto my-auto">
              <b-button size="sm" class="mr-2 py-2 border font-weight-bold" variant="transparent" @click="logout">LogOut</b-button>
            </div>
          </div>
            <hr />
            <div class="row">
              <div class="col my-2" >
                <h6 style="color:gray;" class="text-center mb-3">EMAIL</h6>
                <p class="mb-0 text-center">{{profileData.email}}</p>
              </div>
              <div class="col my-2" style="border-left:1px solid lightgray;border-right:1px solid lightgray;">
                <h6 style="color:gray;" class="text-center mb-3">AGE</h6>
                <p class="text-center mr-1 mb-0 text-secondary">{{profileData.age}}세</p>
              </div>
              <div class="col my-2">
                <h6 style="color:gray;" class="text-center mb-3">GENDER</h6>
                <p v-if="profileData.gender=='1'" class="mb-0 text-center text-primary"><i class="fas fa-mars"></i> Man</p>
                <p v-if="profileData.gender=='0'" class="mb-0 text-center text-danger"><i class="fas fa-venus"></i> Woman</p>
              </div>
            </div>
        </div>
      <br>
      <div class="card pt-2 border mb-5">
        <div class="row text-center p-3" style="cursor:pointer;">
          <div class="col" @click="giveFlag(1)" style="border-right:1px solid lightgray;">
            <img style="width:45px;" src="data:image/svg+xml;base64,PHN2ZyBpZD0iTGF5ZXJfMSIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgNDk3IDQ5NyIgaGVpZ2h0PSI1MTIiIHZpZXdCb3g9IjAgMCA0OTcgNDk3IiB3aWR0aD0iNTEyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Im00NjkuMzU4IDE5Ni42MDljMi4yMzgtMjkuNTIxLTI2LjUwMi01MS41NC01NC40MjUtNDEuNjM0LTkuMzg4LTE1LjcwNi0yNy4yOTYtMjIuNjUyLTQzLjg1Mi0xOS4wMjYgMjkuNDMtMTYuNjEgMjYuOTY4LTYyLjU4Ni03LjI1OC03NC4zMzUgMi4yMzktMjkuNTIxLTI2LjUwMi01MS41NDEtNTQuNDI1LTQxLjYzNC0xMi44Ni0yMS41MTUtNDEuNzEyLTI2LjYxNi02MS4xNjgtMTAuNTc5LTYxLjUxIDI0LjE5My0xMDEuOTUzIDgzLjU1OS0xMDEuOTUzIDE0OS42NTV2MTcwLjExOWMxOC44OTMgMTIuNjMxIDQ1LjU1OSA3LjUxOCA1Ny44NzQtMTMuMTUzIDE2LjcyOCA1LjkwMSAzMy44NjQuMjYzIDQ0LjM1MS0xMS42MDggMTAuNDYzIDExLjkzMSAyNy42MSAxNy42MTkgNDQuNDI4IDExLjY2NyAxMi45MzggMjEuNzI3IDQyLjA4NSAyNi40MDEgNjEuMTQ1IDEwLjY3NiAxOC45NTUgMTUuNjExIDQ4LjEwMSAxMS4xNTkgNjEuMTQ1LTEwLjczNSAyNy44MTggOS44MTMgNTYuNzkzLTEyLjI1OCA1NC4zNzYtNDEuOTAzIDM2LjY0Ny0xMi44MTYgMzYuNTA5LTY0Ljg5NC0uMjM4LTc3LjUxeiIgZmlsbD0iI2ZmZGJlMCIvPjxwYXRoIGQ9Im0yNDguMjMxIDkuNDAxYy0xOS4zMDMtMTUuOTA2LTQ4LjMwMS0xMC45MzctNjEuMTU0IDEwLjc0OS0yNy45MzgtOS44MTctNTYuNzMgMTIuMzI3LTU0LjI4MSA0MS45NDMtMzMuOTE2IDExLjg2Ny0zNi4xOTQgNTcuNTk2LTYuNzczIDc0LjA0Ni0xNi42OTUtMy44OTQtMzQuOTg5IDIuOTkxLTQ0LjQ4IDE5LjAwNi0yNy45MzgtOS44MTctNTYuNzMgMTIuMzI2LTU0LjI4MSA0MS45NDMtMzYuNDA1IDEyLjczOC0zNi4zNjUgNjQuNDk3LjIxIDc3LjE3Ni0yLjMyNyAyOS41NzQgMjYuNTAxIDUxLjY4NyA1NC4zOSA0MS44MTYgMTIuOTM4IDIxLjcyNyA0Mi4wODUgMjYuNDAxIDYxLjE0NSAxMC42NzYgMS4wNTkuODcyIDIuMTUzIDEuNjcxIDMuMjcxIDIuNDE4bDM5LjMwMy03NS4wMjljNy41LTE0LjMxOCAxMS40MTgtMzAuMjQgMTEuNDE4LTQ2LjQwM3YtOTMuMTgyYy4wMDEtNDEuMDY1IDE4Ljg5NS03OS44NDcgNTEuMjMyLTEwNS4xNTl6IiBmaWxsPSIjZmZiNWMwIi8+PHBhdGggZD0ibTQzNS42NCAyMzkuMzQ2Yy03Ljc3LTE0LjYzMy0yNS45My0yMC4xOTYtNDAuNTY1LTEyLjQyOWwtMzIuMjkgMTcuMTQ1LTE3LjE0NS0zMi4yOTFjLTcuNzctMTQuNjM0LTI1LjkzMy0yMC4xOTYtNDAuNTY1LTEyLjQyOS0xNC42MzQgNy43NzEtMjAuMTk4IDI1LjkzMi0xMi40MjkgNDAuNTY1bDI3LjA3NiA1MC45OTUtMTMuNDA0IDQzLjc0OWMtNy43NjkgMjUuMzU0LTMxLjIzMyA0Mi42NzMtNTcuODE3IDQyLjY3My00LjQ4OCAwLTguODg0LS41MDUtMTMuMTM0LTEuNDQ3aC0yOS44Njh2MTIxLjEyM2gxNjQuMjE2YzUuMTU5IDAgOC44MDQtNS4wODUgNy4wOTEtOS45MzgtMi4zNzMtNi43MjMtNy4wODYtMTIuMzQ1LTEzLjE2NC0xNS44OTYtOS4yMzMtNS4zOTUtMTUuMTQyLTE1LjAzMS0xNS4xNDItMjUuNzAzdi0yMi44NjhjMC0xMy44MjcgMi4wNi0yNy41NzcgNi4xMTEtNDAuODAxbDIzLjk1My03OC4xNzkgNDQuNjQ3LTIzLjcwNGMxNC42MzQtNy43NjkgMjAuMTk4LTI1LjkzMSAxMi40MjktNDAuNTY1eiIgZmlsbD0iI2NlODU3YSIvPjxwYXRoIGQ9Im0yMzUuMzY2IDQ5Ni44NjhjLTYuMzE4LTYuMzAxLTkuODY4LTE0Ljg0Ny05Ljg2OC0yMy43NTh2LTczLjQ3NGMwLTguOTExIDMuNTUtMTcuNDU4IDkuODY4LTIzLjc1OC0yMC43Ny00LjYwOS0zOC4xODEtMjAuMDA2LTQ0LjY4My00MS4yMjZsLTEzLjQwNC00My43NDkgMjcuMDc2LTUwLjk5NWM3Ljc3LTE0LjYzNCAyLjIwNS0zMi43OTUtMTIuNDI5LTQwLjU2NS0xNC42MzMtNy43NjctMzIuNzk1LTIuMjA2LTQwLjU2NSAxMi40MjlsLTE3LjE0NSAzMi4yOTEtMzIuMjktMTcuMTQ1Yy0xNC42MzUtNy43NzEtMzIuNzk3LTIuMjA0LTQwLjU2NSAxMi40MjktNy43NyAxNC42MzQtMi4yMDUgMzIuNzk2IDEyLjQyOSA0MC41NjVsNDQuNjQ3IDIzLjcwNCAyMy45NTMgNzguMTc5YzQuMDUyIDEzLjIyNCA2LjExMSAyNi45NzQgNi4xMTEgNDAuODAxdjIyLjg2OGMwIDEwLjY3Mi01LjkwOCAyMC4zMDgtMTUuMTQyIDI1LjcwMy02LjA3OCAzLjU1MS0xMC43OTEgOS4xNzMtMTMuMTY0IDE1Ljg5Ni0xLjcxMyA0Ljg1NCAxLjkzMSA5LjkzOCA3LjA5MSA5LjkzOGgxMDguMjEzeiIgZmlsbD0iI2M3NzQ2NCIvPjxlbGxpcHNlIGN4PSIxODAuMDkzIiBjeT0iNDQwLjg1MiIgZmlsbD0iI2ZmOGU5ZSIgcng9IjIyLjQ3NCIgcnk9IjE3Ljg5NyIgdHJhbnNmb3JtPSJtYXRyaXgoMSAuMDAzIC0uMDAzIDEgMS4zODIgLS41NjIpIi8+PGVsbGlwc2UgY3g9IjMxNi45MDciIGN5PSI0NDEuMjMzIiBmaWxsPSIjZmY4ZTllIiByeD0iMjIuNDc0IiByeT0iMTcuODk3IiB0cmFuc2Zvcm09Im1hdHJpeCgtMSAtLjAwMyAuMDAzIC0xIDYzMi40MzIgODgzLjQ1NikiLz48ZyBmaWxsPSIjMzEzZDQwIj48cGF0aCBkPSJtMTg0LjUgNDAzLjI5NmMtNC4xNDIgMC03LjUgMy4zNDktNy41IDcuNDh2OS45NzNjMCA0LjEzMSAzLjM1OCA3LjQ4IDcuNSA3LjQ4czcuNS0zLjM0OSA3LjUtNy40OHYtOS45NzNjMC00LjEzMS0zLjM1OC03LjQ4LTcuNS03LjQ4eiIvPjxwYXRoIGQ9Im0zMTIuNSA0MDMuMjk2Yy00LjE0MiAwLTcuNSAzLjM0OS03LjUgNy40OHY5Ljk3M2MwIDQuMTMxIDMuMzU4IDcuNDggNy41IDcuNDhzNy41LTMuMzQ5IDcuNS03LjQ4di05Ljk3M2MwLTQuMTMxLTMuMzU4LTcuNDgtNy41LTcuNDh6Ii8+PHBhdGggZD0ibTI2OC4yMzUgNDE2Ljk5M2MtMy43MzctMS43ODQtOC4yMTUtLjIwNS0xMC4wMDEgMy41MjEtMS42NjYgMy40NzQtNS4yOTEgNS43Mi05LjIzNCA1Ljcycy03LjU2OC0yLjI0NS05LjIzNC01LjcyYy0xLjc4Ny0zLjcyNy02LjI2Ni01LjMwMy0xMC4wMDEtMy41MjEtMy43MzcgMS43ODItNS4zMTggNi4yNDgtMy41MzEgOS45NzQgNC4xNDQgOC42NDIgMTMuMDggMTQuMjI2IDIyLjc2NiAxNC4yMjYgOS42ODcgMCAxOC42MjMtNS41ODQgMjIuNzY2LTE0LjIyNiAxLjc4Ny0zLjcyNi4yMDYtOC4xOTItMy41MzEtOS45NzR6Ii8+PC9nPjxwYXRoIGQ9Im0zMzguNTMgMTk2LjU2N2MwLTE2LjU2OC0xMy40MzEtMzAtMzAtMzBzLTMwIDEzLjQzMi0zMCAzMGMtMTYuNTY5IDAtMzAgMTMuNDMyLTMwIDMwczEzLjQzMSAzMCAzMCAzMGMwIDE2LjU2OCAxMy40MzEgMzAgMzAgMzBzMzAtMTMuNDMyIDMwLTMwYzE2LjU2OSAwIDMwLTEzLjQzMiAzMC0zMHMtMTMuNDMxLTMwLTMwLTMweiIgZmlsbD0iI2ZmYjVjMCIvPjxjaXJjbGUgY3g9IjMwOC41MyIgY3k9IjIyNi41NjciIGZpbGw9IiNmY2UzYTAiIHI9IjExLjQ3Ii8+PHBhdGggZD0ibTIyMS40ODEgODQuNTE4YzAtMTEuMDQ2LTguOTU0LTIwLTIwLTIwcy0yMCA4Ljk1NC0yMCAyMGMtMTEuMDQ2IDAtMjAgOC45NTQtMjAgMjBzOC45NTQgMjAgMjAgMjBjMCAxMS4wNDYgOC45NTQgMjAgMjAgMjBzMjAtOC45NTQgMjAtMjBjMTEuMDQ2IDAgMjAtOC45NTQgMjAtMjBzLTguOTU1LTIwLTIwLTIweiIgZmlsbD0iI2ZmOGU5ZSIvPjxjaXJjbGUgY3g9IjIwMS40ODEiIGN5PSIxMDQuNTE4IiBmaWxsPSIjZmNlM2EwIiByPSIxMS40NyIvPjxwYXRoIGQ9Im0zMjEuNDgxIDY0LjUxOGMwLTExLjA0Ni04Ljk1NC0yMC0yMC0yMHMtMjAgOC45NTQtMjAgMjBjLTExLjA0NiAwLTIwIDguOTU0LTIwIDIwczguOTU0IDIwIDIwIDIwYzAgMTEuMDQ2IDguOTU0IDIwIDIwIDIwczIwLTguOTU0IDIwLTIwYzExLjA0NiAwIDIwLTguOTU0IDIwLTIwcy04Ljk1NC0yMC0yMC0yMHoiIGZpbGw9IiNmZmI1YzAiLz48Y2lyY2xlIGN4PSIzMDEuNDgxIiBjeT0iODQuNTE4IiBmaWxsPSIjZmNlM2EwIiByPSIxMS40NyIvPjxwYXRoIGQ9Im0yMDQuNjQ0IDE4Mi4zNjljLTIuNDg1LTEwLjc2Mi0xMy4yMjQtMTcuNDczLTIzLjk4Ni0xNC45ODgtMTAuNzYzIDIuNDg1LTE3LjQ3MyAxMy4yMjQtMTQuOTg4IDIzLjk4Ni0xMC43NjMgMi40ODUtMTcuNDczIDEzLjIyNC0xNC45ODggMjMuOTg2czEzLjIyNCAxNy40NzMgMjMuOTg2IDE0Ljk4OGMyLjQ4NSAxMC43NjIgMTMuMjI0IDE3LjQ3MyAyMy45ODYgMTQuOTg4czE3LjQ3My0xMy4yMjQgMTQuOTg4LTIzLjk4NmMxMC43NjMtMi40ODUgMTcuNDczLTEzLjIyNCAxNC45ODgtMjMuOTg2cy0xMy4yMjQtMTcuNDczLTIzLjk4Ni0xNC45ODh6IiBmaWxsPSIjZmZkYmUwIi8+PGNpcmNsZSBjeD0iMTg5LjY1NSIgY3k9IjIwNi4zNTYiIGZpbGw9IiNmZmNlNzEiIHI9IjExLjQ3Ii8+PHBhdGggZD0ibTgxLjc0IDM4My4yOTZjMC0xMS4wNDYtOC45NTQtMjAtMjAtMjBzLTIwIDguOTU0LTIwIDIwYy0xMS4wNDYgMC0yMCA4Ljk1NC0yMCAyMHM4Ljk1NCAyMCAyMCAyMGMwIDExLjA0NiA4Ljk1NCAyMCAyMCAyMHMyMC04Ljk1NCAyMC0yMGMxMS4wNDYgMCAyMC04Ljk1NCAyMC0yMHMtOC45NTQtMjAtMjAtMjB6IiBmaWxsPSIjZmZiNWMwIi8+PGNpcmNsZSBjeD0iNjEuNzQiIGN5PSI0MDMuMjk2IiBmaWxsPSIjZmZjZTcxIiByPSIxMS40NyIvPjxwYXRoIGQ9Im00NTkuMTQ5IDQzN2MwLTExLjA0Ni04Ljk1NC0yMC0yMC0yMHMtMjAgOC45NTQtMjAgMjBjLTExLjA0NiAwLTIwIDguOTU0LTIwIDIwczguOTU0IDIwIDIwIDIwYzAgMTEuMDQ2IDguOTU0IDIwIDIwIDIwczIwLTguOTU0IDIwLTIwYzExLjA0NiAwIDIwLTguOTU0IDIwLTIwcy04Ljk1NS0yMC0yMC0yMHoiIGZpbGw9IiNmZjhlOWUiLz48Y2lyY2xlIGN4PSI0MzkuMTQ5IiBjeT0iNDU3IiBmaWxsPSIjZmNlM2EwIiByPSIxMS40NyIvPjwvc3ZnPg==" />
            <p class="mb-0 font-weight-bold mt-1" style="color:hotpink;">SPRING</p>
          </div>
          <div class="col" @click="giveFlag(2)" style="border-right:1px solid lightgray;">
            <img style="width:45px;" src="data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjUxMiIgdmlld0JveD0iMCAwIDUxMiA1MTIiIHdpZHRoPSI1MTIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgaWQ9ImZsYXQiPjxjaXJjbGUgY3g9IjI1NS41MTQiIGN5PSIyNTYuNDU3IiBmaWxsPSIjZWFlYWU4IiByPSIyMjUuNDIzIi8+PHBhdGggZD0ibTMwNC40MzMgMzMzLjI4MyA0My4zOTItMTA4LjQ4M2E1Mi42OTMgNTIuNjkzIDAgMCAxIC0zNy0zNC4zMzhsLTEwNC40NDcgMzAuMzI4YTM0Ny41MzMgMzQ3LjUzMyAwIDAgMCAtMTI3LjYgNjguNDU0bC0zOC45MzggMzIuOTQ5YTIyNS44NDcgMjI1Ljg0NyAwIDAgMCAxNTkuODQ5IDE1Mi43MTQgMzQ3LjU0NSAzNDcuNTQ1IDAgMCAwIDEwNC43NDQtMTQxLjYyNHoiIGZpbGw9IiNkMzJiMzkiLz48cGF0aCBkPSJtNDU2Ljg2NyAxNTUuMDIzYTE5OS40NzEgMTk5LjQ3MSAwIDAgMCAtNTIuNjctMTAuODE0IDUyLjU3OCA1Mi41NzggMCAwIDEgLTkuMjkxIDY5LjU0MiA0MzkuOTQgNDM5Ljk0IDAgMCAxIDU1LjkxMiAxNTUuMzQgMjI1LjcxMSAyMjUuNzExIDAgMCAwIDYuMDQ5LTIxNC4wNjh6IiBmaWxsPSIjNDNkY2ZlIi8+PHBhdGggZD0ibTM1Ni4xMzYgMTIxLjQxMy0xLjA3MS00LjYzOWE1MjIuMDA4IDUyMi4wMDggMCAwIDAgLTIyLjI3Mi03Mi4xNDMgMjI1Ljc1MyAyMjUuNzUzIDAgMCAwIC0yMTUuNDU2IDMzLjcxOSA1MjEuOTY4IDUyMS45NjggMCAwIDEgMjAwLjgxMiA2NC41NjIgNTIuNTMyIDUyLjUzMiAwIDAgMSAzNy45ODctMjEuNDk5eiIgZmlsbD0iI2ZiYjU0MCIvPjxjaXJjbGUgY3g9IjM2MC43MTIiIGN5PSIxNzMuODAxIiBmaWxsPSIjZmJmZGZmIiByPSI1Mi41OTkiLz48L2c+PC9zdmc+" />
            <p class="mb-0 font-weight-bold mt-1" style="color:skyBlue;">SUMMER</p>
          </div>
          <div class="col" @click="giveFlag(3)" style="border-right:1px solid lightgray;">
            <img style="width:45px;" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pg0KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjAuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPg0KPHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJDYXBhXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4Ig0KCSB2aWV3Qm94PSIwIDAgNTEyLjAwMiA1MTIuMDAyIiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA1MTIuMDAyIDUxMi4wMDI7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4NCjxwYXRoIHN0eWxlPSJmaWxsOiNGMDdDM0M7IiBkPSJNNDUwLjA1OCw5Ny4xODJjMzEuNDUsMzEuMjY0LDM4Ljc3OCw3NC42NjYsMTYuMzY3LDk2Ljk0NA0KCWMtMjIuNDExLDIyLjI3OS02Ni4wNzEsMTQuOTkyLTk3LjUyMi0xNi4yN2MtMzEuNDUtMzEuMjY0LTM4Ljc3OS03NC42NjctMTYuMzY2LTk2Ljk0NQ0KCUMzNzQuOTQ1LDU4LjYzMyw0MTguNjA5LDY1LjkxOCw0NTAuMDU4LDk3LjE4MnoiLz4NCjxnIHN0eWxlPSJvcGFjaXR5OjAuMTsiPg0KCTxwYXRoIHN0eWxlPSJmaWxsOiMxQjAwM0Y7IiBkPSJNMzkwLjYzMSwxNzcuODU1Yy0zMS40NS0zMS4yNjQtMzguNzgtNzQuNjY3LTE2LjM2Ny05Ni45NDUNCgkJYzYuMzc4LTYuMzQxLDE0LjQ4MS0xMC4yNzksMjMuNTMyLTExLjk1OWMtMTcuNjA2LTIuOTEtMzQuMDc5LDAuODQzLTQ1LjI2LDExLjk1OWMtMjIuNDEzLDIyLjI3OC0xNS4wODQsNjUuNjgxLDE2LjM2Niw5Ni45NDUNCgkJYzIyLjUsMjIuMzY1LDUxLjI0NCwzMi40NTEsNzMuOTksMjguMjI5QzQyNS4yMTMsMjAzLjE2Miw0MDYuMzksMTkzLjUxOSwzOTAuNjMxLDE3Ny44NTV6Ii8+DQo8L2c+DQo8cGF0aCBzdHlsZT0iZmlsbDojQTUzQzI5OyIgZD0iTTQ4OS40NDIsMjA2LjQzM2wtMzYuNzQzLTM2LjUyNXYtNDQuODQ3YzAtNC4xNDItMy4zNTctNy41LTcuNS03LjVzLTcuNSwzLjM1OC03LjUsNy41djI5LjkzNQ0KCWwtMjguNTYxLTI4LjM5MXYtMjMuMzIyYzAtNC4xNDItMy4zNTctNy41LTcuNS03LjVzLTcuNSwzLjM1OC03LjUsNy41djguNDExbC0xNy4yMjEtMTcuMTE5Yy0yLjkzNi0yLjkyLTcuNjg2LTIuOTA2LTEwLjYwNywwLjAzMQ0KCWMtMi45MiwyLjkzOC0yLjkwNiw3LjY4NywwLjAzMiwxMC42MDZsMTcuMTEsMTcuMDFoLTguNDE1Yy00LjE0MiwwLTcuNDk5LDMuMzU4LTcuNDk5LDcuNTAxYzAsNC4xNDIsMy4zNTgsNy41LDcuNTAxLDcuNDk5DQoJbDIzLjUwMi0wLjAwMWwxNy45MDIsMTcuNzk2aC0zMS40MzFjLTQuMTQzLDAtNy41LDMuMzU4LTcuNSw3LjVzMy4zNTcsNy41LDcuNSw3LjVoNDYuNTJsNDcuMzM0LDQ3LjA1Mw0KCWMxLjQ2MywxLjQ1NSwzLjM3NSwyLjE4MSw1LjI4NywyLjE4MWMxLjkyNywwLDMuODUzLTAuNzM4LDUuMzE5LTIuMjEyQzQ5Mi4zOTUsMjE0LjEwMiw0OTIuMzgxLDIwOS4zNTMsNDg5LjQ0MiwyMDYuNDMzeiIvPg0KPHBhdGggc3R5bGU9ImZpbGw6I0QxNjYwNTsiIGQ9Ik0xNjQuNzg3LDM4NC4yNDFjMzEuMjY1LDMxLjQ1MiwzOC41NDgsNzUuMTE2LDE2LjI3LDk3LjUyNg0KCWMtMjIuMjc3LDIyLjQxMi02NS42NzgsMTUuMDgzLTk2Ljk0Mi0xNi4zNjljLTMxLjI2Mi0zMS40NTEtMzguNTQ3LTc1LjExMy0xNi4yNy05Ny41MjUNCglDOTAuMTIxLDM0NS40NjEsMTMzLjUyNiwzNTIuNzksMTY0Ljc4NywzODQuMjQxeiIvPg0KPGcgc3R5bGU9Im9wYWNpdHk6MC4xOyI+DQoJPHBhdGggc3R5bGU9ImZpbGw6IzFCMDAzRjsiIGQ9Ik0xMDUuNzE4LDQ1NC41NDZjLTMxLjI2My0zMS40NTEtMzguNTQ4LTc1LjExMy0xNi4yNzEtOTcuNTI1YzAuMzYyLTAuMzY0LDAuNzQ1LTAuNjk5LDEuMTE4LTEuMDQ3DQoJCWMtOC43MjcsMS43NTktMTYuNTM5LDUuNjc5LTIyLjcyMSwxMS44OTljLTIyLjI3NywyMi40MTItMTQuOTkyLDY2LjA3NCwxNi4yNyw5Ny41MjVjMzAuNzU3LDMwLjk0MSw3My4yNDIsMzguNTE1LDk1LjgyNSwxNy40MTcNCgkJQzE1Ny4yMjUsNDg3LjM5MywxMjguMzA2LDQ3Ny4yNywxMDUuNzE4LDQ1NC41NDZ6Ii8+DQo8L2c+DQo8cGF0aCBzdHlsZT0iZmlsbDojQTUzQzI5OyIgZD0iTTIwNC4wMDIsNDk0LjIxMmwtMzYuNTQ1LTM2Ljc2NnYtNDUuMTU4YzAtNC4xNDItMy4zNTctNy41LTcuNS03LjVzLTcuNSwzLjM1OC03LjUsNy41djMwLjA2OA0KCWwtMjguMzAxLTI4LjQ3MnYtMjMuNTA1YzAtNC4xNDItMy4zNTctNy41LTcuNS03LjVzLTcuNSwzLjM1OC03LjUsNy41djguNDE0bC0xNy4wMDktMTcuMTExYy0yLjkyLTIuOTM4LTcuNjY5LTIuOTUxLTEwLjYwNy0wLjAzMg0KCWMtMi45MzgsMi45Mi0yLjk1Miw3LjY2OS0wLjAzMiwxMC42MDdsMTcuMTE3LDE3LjIyMWwtOC40MSwwLjAwMWMtNC4xNDMsMC03LjUsMy4zNTctNy41LDcuNWMwLDQuMTQyLDMuMzU4LDcuNSw3LjUsNy41DQoJbDIzLjMxOS0wLjAwMWwxNy44ODUsMTcuOTkzaC0zMS4yODZjLTQuMTQzLDAtNy41LDMuMzU4LTcuNSw3LjVzMy4zNTcsNy41LDcuNSw3LjVoNDYuMTk2bDQ3LjAzMyw0Ny4zMTgNCgljMS40NjYsMS40NzUsMy4zOTMsMi4yMTMsNS4zMTksMi4yMTNjMS45MTIsMCwzLjgyNC0wLjcyNyw1LjI4Ny0yLjE4MUMyMDYuOTA3LDUwMS44OTgsMjA2LjkyMiw0OTcuMTUsMjA0LjAwMiw0OTQuMjEyeiIvPg0KPHBhdGggc3R5bGU9ImZpbGw6I0Y3OTMxRTsiIGQ9Ik0xNTcuNzcsMzI1LjUwN2MtMC45MDcsMC0xLjgxMy0wLjIzOS0yLjYxNy0wLjcxMWMtMTQuNjU4LTguNjAyLTI4Ljc1OC0yNi42NTEtMzguNjgyLTQ5LjUyMg0KCWMtOS40MzgtMjEuNzQ2LTEyLjIxNy00MS4wNDctOC4yNjItNTcuMzY3Yy00LjgxMSwxLjE1Mi05Ljk0NiwxLjczNy0xNS4yNjgsMS43MzdjLTEyLjc3MSwwLTI3LjA1LTMuMzQ3LTQyLjQzOS05Ljk0Nw0KCWMtMjIuOTU5LTkuODQ0LTQxLjEtMjMuODMtNDkuNzcxLTM4LjM3M2MtMC44NS0xLjQyNS0wLjk2NS0zLjE3MS0wLjMxMS00LjY5NmMwLjY1NS0xLjUyNCwyLTIuNjQyLDMuNjE4LTMuMDA2DQoJYzQuMzI4LTAuOTc1LDkuMTIxLTEuNDY4LDE0LjI0NC0xLjQ2OGMxMS42OTksMCwyNS4xMzksMi41OTksMzguODY1LDcuNTE2Yy0yLjk2OS0zLjU4OC01Ljc5Mi03LjIyNy04LjM5My0xMC44MTYNCgljLTE5LjY3LTI3LjE0Mi0yOC44NDktNTIuNzk5LTI3LjI4Mi03Ni4yNmMwLjEwMy0xLjUzNywwLjg4Ni0yLjk1LDIuMTM1LTMuODUyYzAuODkxLTAuNjQyLDEuOTUxLTAuOTc5LDMuMDI3LTAuOTc5DQoJYzAuNDM0LDAsMC44NzEsMC4wNTUsMS4zLDAuMTY1YzIyLjcwNyw1Ljg5Nyw0NC4xNCwyMi40NzUsNjMuNzAzLDQ5LjI3NWMtMC4wODMtMi43MzMtMC4xMjQtNS4xOTctMC4xMjQtNy41Mw0KCWMwLTQ1LjU3NSwxMS4xMzMtOTAuODM3LDI3LjcwMy0xMTIuNjMyQzEyMC4xOTYsNS43NTYsMTIxLjcyLDUsMTIzLjMzNSw1YzEuNjE2LDAsMy4xMzksMC43NTUsNC4xMTgsMi4wNDINCgljMTYuNTcsMjEuNzkyLDI3LjcwNCw2Ny4wNTQsMjcuNzA0LDExMi42MzJsLTAuMDA2LDEuMTA1YzMuODA1LTQuMzIyLDcuODU3LTguNjEsMTIuMDQ2LTEyLjc3NA0KCWMzNC43NDktMzQuNTQxLDczLjA4OS01Ni4wMDMsMTA1LjE4OS01OC44ODNjMC4xNTMtMC4wMTMsMC4zMDktMC4wMiwwLjQ2Mi0wLjAyYzEuMzY3LDAsMi42ODYsMC41NDIsMy42NjEsMS41MTgNCgljMS4wODQsMS4wODYsMS42MywyLjU5OSwxLjQ5MSw0LjEyOGMtMi45MTIsMzEuOTAyLTI0LjUwMSw2OS45OTgtNTkuMjMsMTA0LjUyM2MtMy42NTYsMy42MzMtNy40Miw3LjE3Ny0xMS4xODksMTAuNTMyDQoJYzIyLjkzNywwLjE3LDQ3LjI2LDMuMTcyLDY4LjQ5MSw4LjQ0OWMxOS41OTQsNC44NzIsMzUuMzYzLDExLjQ0Nyw0NS42MDQsMTkuMDE0YzEuMzE3LDAuOTc0LDIuMDk2LDIuNTE1LDIuMSw0LjE1NQ0KCWMwLjAwMywxLjYzOS0wLjc3MSwzLjE4My0yLjA4Niw0LjE2MmMtMjQuMjI2LDE4LjAzNC03Ni43NTQsMjcuNDctMTE2LjEyLDI3LjQ3Yy0yLjUwNywwLTUuMTEtMC4wNDYtOC4xOTUtMC4xNDZsMC43MzMsMC41MDgNCgljMC4yNDQsMC4xNjgsMC40ODgsMC4zMzYsMC43MzEsMC41MTFjMjcuMywxOS41NSw0NC4xODEsNDAuOTg4LDUwLjE3MSw2My43MThjMC4zOTUsMS40OTUsMC4xLDMuMDg3LTAuODAzLDQuMzQyDQoJYy0wLjkwMiwxLjI1NC0yLjMxNiwyLjA0LTMuODU4LDIuMTQzYy0xLjczLDAuMTE0LTMuNDg1LDAuMTcyLTUuMjIxLDAuMTcyYy0yMi4xNjQtMC4wMDEtNDYuMjI0LTkuMTgyLTcxLjUxMi0yNy4yODkNCgljLTMuNjI5LTIuNi03LjI4OS01LjQwNy0xMC44OC04LjM0NGM3LjE2OCwxOS43NzUsOS4zMjYsMzguNTMxLDYuMDc3LDUyLjgxMmMtMC4zNjYsMS42MDktMS40NzcsMi45NDctMi45ODksMy42MDINCglDMTU5LjE2NiwzMjUuMzY2LDE1OC40NjcsMzI1LjUwNywxNTcuNzcsMzI1LjUwN3oiLz4NCjxnIHN0eWxlPSJvcGFjaXR5OjAuMTsiPg0KCTxwYXRoIHN0eWxlPSJmaWxsOiMxQjAwM0Y7IiBkPSJNMTM3LjU5NywyNTQuMDU1Yy05LjQzOS0yMS43NDYtMTIuMjE4LTQxLjA0Ny04LjI2Mi01Ny4zNjdjLTQuODExLDEuMTUyLTkuOTQ2LDEuNzM3LTE1LjI2OCwxLjczNw0KCQljLTEyLjc3MSwwLTI3LjA1LTMuMzQ3LTQyLjQzOS05Ljk0OGMtMTUuODgtNi44MDktMjkuNDQ5LTE1LjYtMzkuMTgtMjUuMTg1Yy00LjkyMy0wLjc1LTkuNjczLTEuMTM3LTE0LjE2NS0xLjEzNw0KCQljLTUuMTIzLDAtOS45MTYsMC40OTQtMTQuMjQ0LDEuNDY4Yy0xLjYxOCwwLjM2NC0yLjk2MywxLjQ4Mi0zLjYxOCwzLjAwNmMtMC42NTQsMS41MjUtMC41MzksMy4yNywwLjMxMSw0LjY5Ng0KCQljOC42NzEsMTQuNTQyLDI2LjgxMSwyOC41MjksNDkuNzcxLDM4LjM3M2MxNS4zOSw2LjYwMSwyOS42NjksOS45NDcsNDIuNDM5LDkuOTQ3YzUuMzIxLDAsMTAuNDU3LTAuNTg0LDE1LjI2OC0xLjczNw0KCQljLTMuOTU1LDE2LjMyLTEuMTc3LDM1LjYyMSw4LjI2Miw1Ny4zNjdjOS45MjQsMjIuODcsMjQuMDIzLDQwLjkxOSwzOC42ODIsNDkuNTIyYzAuODA1LDAuNDcyLDEuNzEsMC43MTEsMi42MTcsMC43MTENCgkJYzAuNjk3LDAsMS4zOTYtMC4xNDEsMi4wNTUtMC40MjZjMS41MTMtMC42NTUsMi42MjMtMS45OTMsMi45ODktMy42MDJjMS44NTktOC4xNzMsMS45MzktMTcuODE1LDAuMzMxLTI4LjI3Mg0KCQlDMTUzLjQyMSwyODMuNTIxLDE0NC40OTgsMjY5Ljk1OSwxMzcuNTk3LDI1NC4wNTV6Ii8+DQo8L2c+DQo8cGF0aCBzdHlsZT0iZmlsbDojQTUzQzI5OyIgZD0iTTIzMC4zMTMsMjAwLjQ2NmMtMC4yODQtNC4xMzMtMy44Ni03LjI1Mi03Ljk5NS02Ljk3bC04NC43NTYsNS44MDlsODMuNTYtODMuMDYzDQoJYzIuOTM4LTIuOTIsMi45NTItNy42NjgsMC4wMzItMTAuNjA2cy03LjY2OS0yLjk1MS0xMC42MDYtMC4wMzJsLTg0LjQzNCw4My45MzJsMi45MjYtOTEuNTY4YzAuMTMzLTQuMTQtMy4xMTYtNy42MDMtNy4yNTctNy43MzUNCgljLTQuMTQzLTAuMTIxLTcuNjAzLDMuMTE2LTcuNzM1LDcuMjU2bC0zLjAyLDk0LjUyMkw4Mi42NDYsMTQ3LjI3Yy0yLjIxOS0zLjQ5OC02Ljg1Mi00LjUzNC0xMC4zNTEtMi4zMTUNCgljLTMuNDk4LDIuMjE5LTQuNTM0LDYuODUzLTIuMzE1LDEwLjM1MWwzNS4wMjUsNTUuMjE1bC00OC4xNiw0Ny44NzZjLTIuOTM4LDIuOTItMi45NTIsNy42NjktMC4wMzIsMTAuNjA2DQoJYzEuNDY2LDEuNDc1LDMuMzkzLDIuMjEyLDUuMzE5LDIuMjEyYzEuOTEyLDAsMy44MjQtMC43MjcsNS4yODctMi4xODFsNDguMTg0LTQ3Ljg5OGw2MS44MzYsMzkuMjkzDQoJYzEuMjQ3LDAuNzkzLDIuNjQsMS4xNzEsNC4wMTYsMS4xNzFjMi40OCwwLDQuOTA4LTEuMjMsNi4zMzctMy40NzhjMi4yMjItMy40OTYsMS4xODktOC4xMzEtMi4zMDgtMTAuMzUzbC01Mi4xNS0zMy4xMzgNCglsOTAuMDEtNi4xNjlDMjI3LjQ3NiwyMDguMTc4LDIzMC41OTYsMjA0LjU5OCwyMzAuMzEzLDIwMC40NjZ6Ii8+DQo8cGF0aCBzdHlsZT0iZmlsbDojRkZDNTU0OyIgZD0iTTQ3Mi41MzgsNDQzLjU2N2MtNDQuMjg1LDQ0LjI4NS0xMDguMjUzLDUyLjM3Ni0xNDIuNTkzLDE4LjAzNA0KCWMtMTcuNjQ1LTE3LjY0NC0yNC44MzktNDQuMjA3LTE5LjczOC03Mi44NzhjMC4xNDYtMC44LDEzLjk1Mi03Ny4wNDYtMTAuOTkxLTExMi40NjNjLTEuMDk0LTEuNTUyLTEuMDM0LTMuNjQ0LDAuMTQ2LTUuMTQzDQoJYzAuMTA5LTAuMTQsMC4yMjUtMC4yNjgsMC4zNDYtMC4zODhjMS4yMDQtMS4yMDYsMy4wMTktMS42MDQsNC42MjUtMC45NzZjMC4zNSwwLjEzNSwzNi42NzcsMTMuNzM3LDEyMS4xODUsOC4xNjENCgljMS42NDQtMC4yNDQsMTEuODg1LTEuNjIsMjQuNjQ3LTAuMDZjMTguMzc2LDIuMjQsMzMuMiw5LjU3Miw0Mi44NzYsMjEuMTk1YzE1LjI1NiwxOC4zMywyMS42MjcsNDMuMTk2LDE3Ljk0MSw3MC4wMjMNCglDNTA3LjI3NiwzOTYuMDI0LDQ5My42MjMsNDIyLjQ3OCw0NzIuNTM4LDQ0My41Njd6Ii8+DQo8ZyBzdHlsZT0ib3BhY2l0eTowLjE7Ij4NCgk8cGF0aCBzdHlsZT0iZmlsbDojMUIwMDNGOyIgZD0iTTM2Mi41MzcsNDYxLjYwMmMtMTcuNjQ1LTE3LjY0NC0yNC44MzgtNDQuMjA3LTE5LjczOC03Mi44NzgNCgkJYzAuMTQ2LTAuOCwxMy45NTItNzcuMDQ2LTEwLjk5MS0xMTIuNDYzYy0wLjEyNC0wLjE3OC0wLjIzLTAuMzYyLTAuMzI0LTAuNTUyYy0xOC4zOTItMi42NzMtMjYuOTgxLTUuODktMjcuMTUxLTUuOTU1DQoJCWMtMS42MDYtMC42MjktMy40MjEtMC4yMy00LjYyNSwwLjk3NmMtMC4xMjEsMC4xMi0wLjIzNiwwLjI0OC0wLjM0NiwwLjM4OGMtMS4xOCwxLjUtMS4yMzksMy41OTItMC4xNDYsNS4xNDMNCgkJYzI0Ljk0MywzNS40MTcsMTEuMTM3LDExMS42NjMsMTAuOTkxLDExMi40NjNjLTUuMTAxLDI4LjY3MSwyLjA5NCw1NS4yMzQsMTkuNzM4LDcyLjg3OA0KCQljMTguMDU0LDE4LjA1NSw0NC4yOTcsMjQuMzc0LDcxLjU2MywxOS44NzhDMzg2LjY1NCw0NzguOCwzNzMuMTczLDQ3Mi4yMzgsMzYyLjUzNyw0NjEuNjAyeiIvPg0KPC9nPg0KPHBhdGggc3R5bGU9ImZpbGw6I0YwN0MzQzsiIGQ9Ik00OTYuNzc2LDQ1NC44NTFsLTYxLjQ4Ny02MS40OWMxMy42MDQtMjMuNTMxLDEwLjMtNDQuNzUyLDEwLjE0MS00NS43MDkNCgljLTAuNjc3LTQuMDctNC41MDgtNi44MDYtOC41ODUtNi4xNTRjLTQuMDczLDAuNjU1LTYuODUxLDQuNDk4LTYuMjE5LDguNTc1YzAuMTA3LDAuNjkyLDIuMTg1LDE1LjA5Ny02LjM5OCwzMi4yMjVsLTI1LjA3LTI1LjA3MQ0KCWMxMS4yMTMtMTkuODE2LDMuOTQxLTQxLjU0MiwzLjYyNi00Mi40NTljLTEuMzQ2LTMuOTA1LTUuNTg0LTUuOTczLTkuNDk4LTQuNjQ1Yy0zLjkxLDEuMzI4LTYuMDA2LDUuNTgyLTQuNjk1LDkuNDk4DQoJYzAuMDUsMC4xNDcsNC40MTcsMTMuNTU1LTAuNjU3LDI2LjM4MWwtMjcuNzI1LTI3LjcyNmMtMi45MjktMi45MjktNy42NzgtMi45My0xMC42MDYsMGMtMi45MywyLjkyOS0yLjkzLDcuNjc3LTAuMDAxLDEwLjYwNg0KCWw0Ni4zNzUsNDYuMzc3Yy0xNS44NzQsNC41MDItMzEuMDQ3LTAuNDM5LTMxLjMxOC0wLjUzYy0zLjkwOS0xLjMzMy04LjE2NiwwLjc0OC05LjUxMyw0LjY1N2MtMS4zNDksMy45MTcsMC43MzMsOC4xODUsNC42NSw5LjUzMw0KCWMwLjY1LDAuMjI0LDkuNzE0LDMuMjYyLDIxLjk2MiwzLjI2MmM3LjgsMCwxNi44OTItMS4yNDQsMjUuOTIyLTUuMjE5bDI1LjE4NCwyNS4xODVjLTI4LjYxOSwxNC42NzItNTUuMzU5LDkuMjAyLTU1LjgxMyw5LjEwNA0KCWMtNC4wMzMtMC44OTEtOC4wMzQsMS42NS04LjkzOCw1LjY4NWMtMC45MDUsNC4wNDIsMS42MzgsOC4wNTIsNS42OCw4Ljk1OGMwLjYyNCwwLjE0LDYuOTY2LDEuNDk5LDE2Ljc0MywxLjQ5OQ0KCWMxMy4zNDUsMCwzMy4wODctMi41NDMsNTMuMzk2LTE0LjE3N2w0Mi4yMzgsNDIuMjRjMS40NjUsMS40NjUsMy4zODQsMi4xOTcsNS4zMDQsMi4xOTdjMS45MTksMCwzLjgzOS0wLjczMiw1LjMwMy0yLjE5Nw0KCUM0OTkuNzA1LDQ2Mi41MjgsNDk5LjcwNSw0NTcuNzgsNDk2Ljc3Niw0NTQuODUxeiIvPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPC9zdmc+DQo=" />
            <p class="mb-0 font-weight-bold mt-1" style="color:IndianRed;">AUTUMN</p>
          </div>
          <div class="col" @click="giveFlag(4)">
            <img style="width:45px;" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pg0KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjAuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPg0KPHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJDYXBhXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4Ig0KCSB2aWV3Qm94PSIwIDAgNTEyLjAwMyA1MTIuMDAzIiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA1MTIuMDAzIDUxMi4wMDM7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4NCjxwYXRoIHN0eWxlPSJmaWxsOiM4MEM3RUE7IiBkPSJNNTEyLjAwMiwyNTZjMC03LjQxNS02LjAxMS0xMy40MjctMTMuNDI3LTEzLjQyN2gtMjEuMTI3bDIwLjExMy0yMC4xMTMNCgljNS4yNDQtNS4yNDQsNS4yNDQtMTMuNzQ2LDAtMTguOTg5cy0xMy43NDUtNS4yNDQtMTguOTg5LDBsLTM5LjEwMywzOS4xMDNoLTE5Ljg3NWwyMC4xMTMtMjAuMTEzDQoJYzUuMjQ0LTUuMjQ0LDUuMjQ0LTEzLjc0NiwwLTE4Ljk4OWMtNS4yNDUtNS4yNDQtMTMuNzQ2LTUuMjQ0LTE4Ljk4OSwwbC0zOS4xMDMsMzkuMTAzaC05My4xOTdsNjUuOTAxLTY1LjkwMWg1NS4yOTkNCgljNy40MTYsMCwxMy40MjctNi4wMTEsMTMuNDI3LTEzLjQyN3MtNi4wMTEtMTMuNDI3LTEzLjQyNy0xMy40MjdoLTI4LjQ0NGwxNC4wNTQtMTQuMDU0aDU1LjI5OWM3LjQxNiwwLDEzLjQyNy02LjAxMSwxMy40MjctMTMuNDI3DQoJYzAtNy40MTYtNi4wMTEtMTMuNDI3LTEzLjQyNy0xMy40MjdoLTI4LjQ0NGwxNC45NC0xNC45NGM1LjI0NC01LjI0NCw1LjI0NC0xMy43NDYsMC0xOC45ODljLTUuMjQ0LTUuMjQ0LTEzLjc0Ni01LjI0NC0xOC45ODksMA0KCWwtMTQuOTQsMTQuOTRWNjEuNDc1YzAtNy40MTYtNi4wMTEtMTMuNDI3LTEzLjQyNy0xMy40MjdzLTEzLjQyNyw2LjAxMS0xMy40MjcsMTMuNDI3djU1LjI5OWwtMTQuMDU0LDE0LjA1NHYtMjguNDQzDQoJYzAtNy40MTYtNi4wMTEtMTMuNDI3LTEzLjQyNy0xMy40MjdjLTcuNDE2LDAtMTMuNDI3LDYuMDExLTEzLjQyNywxMy40Mjd2NTUuMjk5bC02NS45MDEsNjUuOTAxdi05My4xOTdsMzkuMTAzLTM5LjEwMw0KCWM1LjI0NC01LjI0NCw1LjI0NC0xMy43NDYsMC0xOC45ODljLTUuMjQ1LTUuMjQ0LTEzLjc0Ni01LjI0NC0xOC45ODksMGwtMjAuMTE0LDIwLjExM1Y3Mi41MzNsMzkuMTAzLTM5LjEwMw0KCWM1LjI0NC01LjI0NCw1LjI0NC0xMy43NDYsMC0xOC45ODljLTUuMjQ1LTUuMjQ0LTEzLjc0Ni01LjI0NC0xOC45ODksMGwtMjAuMTE0LDIwLjExM1YxMy40MjdDMjY5LjQyOSw2LjAxMSwyNjMuNDE4LDAsMjU2LjAwMiwwDQoJYy03LjQxNSwwLTEzLjQyNyw2LjAxMS0xMy40MjcsMTMuNDI3djIxLjEyN2wtMjAuMTEzLTIwLjExM2MtNS4yNDQtNS4yNDQtMTMuNzQ1LTUuMjQ0LTE4Ljk4OSwwDQoJYy01LjI0NCw1LjI0NC01LjI0NCwxMy43NDYsMCwxOC45ODlsMzkuMTAzLDM5LjEwM3YxOS44NzZsLTIwLjExMy0yMC4xMTNjLTUuMjQ0LTUuMjQ0LTEzLjc0NS01LjI0NC0xOC45ODksMA0KCWMtNS4yNDQsNS4yNDQtNS4yNDQsMTMuNzQ2LDAsMTguOTg5bDM5LjEwMywzOS4xMDN2OTMuMTk3bC02NS45MDEtNjUuOTAxdi01NS4zYzAtNy40MTYtNi4wMTEtMTMuNDI3LTEzLjQyNy0xMy40MjcNCglzLTEzLjQyNyw2LjAxMS0xMy40MjcsMTMuNDI3djI4LjQ0NGwtMTQuMDU0LTE0LjA1NHYtNTUuM2MwLTcuNDE2LTYuMDExLTEzLjQyNy0xMy40MjctMTMuNDI3Yy03LjQxNiwwLTEzLjQyNyw2LjAxMS0xMy40MjcsMTMuNDI3DQoJdjI4LjQ0NEw5My45NzIsNzQuOTgxYy01LjI0NC01LjI0NC0xMy43NDYtNS4yNDQtMTguOTg5LDBjLTUuMjQ0LDUuMjQ0LTUuMjQ0LDEzLjc0NiwwLDE4Ljk4OWwxNC45NCwxNC45NEg2MS40NzcNCgljLTcuNDE2LDAtMTMuNDI3LDYuMDExLTEzLjQyNywxMy40MjdzNi4wMTEsMTMuNDI3LDEzLjQyNywxMy40MjdoNTUuMjk5bDE0LjA1NCwxNC4wNTRoLTI4LjQ0Mw0KCWMtNy40MTYsMC0xMy40MjcsNi4wMTEtMTMuNDI3LDEzLjQyN3M2LjAxMSwxMy40MjcsMTMuNDI3LDEzLjQyN2g1NS4yOTlsNjUuOTAxLDY1LjkwMWgtOTMuMTk3TDkxLjI4NiwyMDMuNDcNCgljLTUuMjQ0LTUuMjQ0LTEzLjc0NS01LjI0NC0xOC45ODksMGMtNS4yNDQsNS4yNDQtNS4yNDQsMTMuNzQ2LDAsMTguOTg5bDIwLjExMywyMC4xMTNINzIuNTM1TDMzLjQzMiwyMDMuNDcNCgljLTUuMjQ0LTUuMjQ0LTEzLjc0NS01LjI0NC0xOC45ODksMGMtNS4yNDQsNS4yNDQtNS4yNDQsMTMuNzQ2LDAsMTguOTg5bDIwLjExMywyMC4xMTNIMTMuNDI5Yy03LjQxNiwwLTEzLjQyNyw2LjAxMi0xMy40MjcsMTMuNDI3DQoJYzAsNy40MTYsNi4wMTEsMTMuNDI3LDEzLjQyNywxMy40MjdoMjEuMTI4bC0yMC4xMTMsMjAuMTE0Yy01LjI0NCw1LjI0NC01LjI0NCwxMy43NDYsMCwxOC45ODkNCgljMi42MjIsMi42MjIsNi4wNTgsMy45MzMsOS40OTQsMy45MzNzNi44NzMtMS4zMTEsOS40OTQtMy45MzNsMzkuMTAzLTM5LjEwM2gxOS44NzZsLTIwLjExMywyMC4xMTQNCgljLTUuMjQ0LDUuMjQ0LTUuMjQ0LDEzLjc0NiwwLDE4Ljk4OWMyLjYyMiwyLjYyMiw2LjA1OCwzLjkzMyw5LjQ5NCwzLjkzM3M2Ljg3My0xLjMxMSw5LjQ5NC0zLjkzM2wzOS4xMDMtMzkuMTAzaDkzLjE5Nw0KCWwtNjUuOTAxLDY1LjkwMWgtNTUuMjk5Yy03LjQxNiwwLTEzLjQyNyw2LjAxMS0xMy40MjcsMTMuNDI3YzAsNy40MTYsNi4wMTEsMTMuNDI3LDEzLjQyNywxMy40MjdoMjguNDQ0bC0xNC4wNTQsMTQuMDU0aC01NS4zDQoJYy03LjQxNiwwLTEzLjQyNyw2LjAxMS0xMy40MjcsMTMuNDI3czYuMDExLDEzLjQyNywxMy40MjcsMTMuNDI3aDI4LjQ0NGwtMTQuOTQsMTQuOTRjLTUuMjQ0LDUuMjQ0LTUuMjQ0LDEzLjc0NSwwLDE4Ljk4OQ0KCWMyLjYyMiwyLjYyMiw2LjA1OCwzLjkzMyw5LjQ5NCwzLjkzM3M2Ljg3My0xLjMxMSw5LjQ5NC0zLjkzM2wxNC45NC0xNC45NHYyOC40NDRjMCw3LjQxNiw2LjAxMSwxMy40MjcsMTMuNDI3LDEzLjQyNw0KCWM3LjQxNiwwLDEzLjQyNy02LjAxMSwxMy40MjctMTMuNDI3di01NS4yOTlsMTQuMDU0LTE0LjA1NHYyOC40NDRjMCw3LjQxNiw2LjAxMSwxMy40MjcsMTMuNDI3LDEzLjQyN3MxMy40MjctNi4wMTEsMTMuNDI3LTEzLjQyNw0KCXYtNTUuMjk5bDY1LjkwMS02NS45MDF2OTMuMTk3bC0zOS4xMDMsMzkuMTAzYy01LjI0NCw1LjI0NC01LjI0NCwxMy43NDYsMCwxOC45ODljNS4yNDQsNS4yNDQsMTMuNzQ2LDUuMjQ0LDE4Ljk4OSwwbDIwLjExMy0yMC4xMTMNCgl2MTkuODc1bC0zOS4xMDMsMzkuMTAzYy01LjI0NCw1LjI0NC01LjI0NCwxMy43NDYsMCwxOC45ODljMi42MjIsMi42MjIsNi4wNTgsMy45MzMsOS40OTQsMy45MzNjMy40MzcsMCw2Ljg3My0xLjMxMSw5LjQ5NC0zLjkzMw0KCWwyMC4xMTMtMjAuMTEzdjIxLjEyN2MwLDcuNDE2LDYuMDEyLDEzLjQyNywxMy40MjcsMTMuNDI3YzcuNDE2LDAsMTMuNDI3LTYuMDExLDEzLjQyNy0xMy40Mjd2LTIxLjEyN2wyMC4xMTQsMjAuMTE0DQoJYzUuMjQ0LDUuMjQ0LDEzLjc0Niw1LjI0NCwxOC45ODksMHM1LjI0NC0xMy43NDUsMC0xOC45ODlsLTM5LjEwMy0zOS4xMDN2LTE5Ljg3NmwyMC4xMTQsMjAuMTE0DQoJYzIuNjIyLDIuNjIyLDYuMDU5LDMuOTMzLDkuNDk0LDMuOTMzczYuODczLTEuMzExLDkuNDk0LTMuOTMzYzUuMjQ0LTUuMjQ0LDUuMjQ0LTEzLjc0NSwwLTE4Ljk4OWwtMzkuMTAzLTM5LjEwM1YyODguNDINCglsNjUuOTAxLDY1LjkwMXY1NS4yOTljMCw3LjQxNiw2LjAxMSwxMy40MjcsMTMuNDI3LDEzLjQyN2M3LjQxNiwwLDEzLjQyNy02LjAxMSwxMy40MjctMTMuNDI3di0yOC40NDRsMTQuMDU0LDE0LjA1NHY1NS4yOTkNCgljMCw3LjQxNiw2LjAxMSwxMy40MjcsMTMuNDI3LDEzLjQyN3MxMy40MjctNi4wMTEsMTMuNDI3LTEzLjQyN3YtMjguNDQ0bDE0Ljk0LDE0Ljk0YzIuNjIyLDIuNjIyLDYuMDU5LDMuOTMzLDkuNDk0LDMuOTMzDQoJYzMuNDM3LDAsNi44NzMtMS4zMTEsOS40OTQtMy45MzNjNS4yNDQtNS4yNDQsNS4yNDQtMTMuNzQ1LDAtMTguOTg5bC0xNC45NC0xNC45NGgyOC40NDRjNy40MTYsMCwxMy40MjctNi4wMTEsMTMuNDI3LTEzLjQyNw0KCWMwLTcuNDE2LTYuMDExLTEzLjQyNy0xMy40MjctMTMuNDI3aC01NS4yOTlsLTE0LjA1NC0xNC4wNTRoMjguNDQ0YzcuNDE2LDAsMTMuNDI3LTYuMDExLDEzLjQyNy0xMy40MjcNCgljMC03LjQxNi02LjAxMS0xMy40MjctMTMuNDI3LTEzLjQyN2gtNTUuMjk5bC02NS45MDEtNjUuOTAxaDkzLjE5N2wzOS4xMDMsMzkuMTAzYzIuNjIyLDIuNjIyLDYuMDU5LDMuOTMzLDkuNDk0LDMuOTMzDQoJczYuODczLTEuMzExLDkuNDk0LTMuOTMzYzUuMjQ0LTUuMjQ0LDUuMjQ0LTEzLjc0NSwwLTE4Ljk4OWwtMjAuMTE0LTIwLjExNGgxOS44NzZsMzkuMTAzLDM5LjEwMw0KCWMyLjYyMiwyLjYyMiw2LjA1OSwzLjkzMyw5LjQ5NCwzLjkzM2MzLjQzNiwwLDYuODczLTEuMzExLDkuNDk0LTMuOTMzYzUuMjQ0LTUuMjQ0LDUuMjQ0LTEzLjc0NSwwLTE4Ljk4OWwtMjAuMTE0LTIwLjExNGgyMS4xMjcNCglDNTA1Ljk5LDI2OS40MjcsNTEyLjAwMiwyNjMuNDE2LDUxMi4wMDIsMjU2eiIvPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPC9zdmc+DQo=" />
            <p class="mb-0 font-weight-bold mt-1" style="color:SteelBlue ;">WINTER</p>
          </div>
        </div>
          <!-- 봄 -->
          <div v-if="flag==1" class="text-center py-1" style="background-color:rgba(0,0,0,0.05);">
            <div class="py-5" v-if="springData.length == 0">
              <p class="mb-0">아직 봄 옷이 없어요.</p>
            </div>
            <div v-else>
              <div class="row my-3 mx-1">
                <div class="col-12 col-md-4 col-lg-3 px-1 mb-3 py-1" v-for="item in springData" :key="item.id">
                  <div class="card content" style="border:0;" data-toggle="modal" data-target="#photodetail" @click="photo(item)">
                    <div class="content-overlay">
                    </div>
                    <img class="content-image" style="width:100%;height:40vh;" :src="server_url + item.image" alt="">
                    <div class="content-details fadeIn-bottom">
                      
                      <div class="d-flex justify-content-center my-5">
                        <div class="mr-2" v-for="line in item.adjectiveList" :key="line.id">
                          <b-badge variant="light">{{line}}</b-badge>
                        </div>
                      </div>
                      <div class="d-flex justify-content-center my-2">
                        <b-badge v-if="item.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                        <div v-for="line in item.lineList" :key="line.id">
                          <b-badge v-if="line == 'floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                        </div>
                      </div>
                      <!-- <div class="d-flex justify-content-between mt-5" > -->
                        <!-- <small class="m-0 p-0" style="font-weight:bold;color:white">향수</small> -->
                        <!-- <div  class="p-1 mx-1 bg-white" v-for="perfume in item.perfumedata" :key="perfume.id">
                          <img style="width:50px;height:50px;" :src="perfume.image" alt="">
                        </div>
                      </div> -->
                      <div class="d-flex justify-content-between mt-5" >
                        <div class="mr-2" v-for="perfume in item.perfumedata" :key="perfume.id">
                          <img v-if="perfume.brand == 'Acqua di Parma '" src="../assets/img/acqua_di_parma.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Bulgari '" src="../assets/img/bulgari.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Burberry '" src="../assets/img/burberry.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Byredo '" src="../assets/img/byredo.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Calvin Klein '" src="../assets/img/calvin-klein.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Cartier '" src="../assets/img/cartier.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Chanel '" src="../assets/img/chanel.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Christian Dior '" src="../assets/img/dior.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Creed '" src="../assets/img/creed.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Demeter Fragrance Library '" src="../assets/img/demeter.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Diptyque '" src="../assets/img/diptyque.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Dolce & Gabbana '" src="../assets/img/dolce.jpg" style="width:11rem; height:2rem;">
                          <img v-if="perfume.brand == 'Editions de Parfums Frederic Malle '" src="../assets/img/frederic.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Estée Lauder '" src="../assets/img/estee.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Giorgio Armani '" src="../assets/img/giorgio.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Givenchy '" src="../assets/img/givenchy.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Gucci '" src="../assets/img/gucci.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Hermès '" src="../assets/img/hermes.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Hugo Boss '" src="../assets/img/boss.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Jo Malone London '" src="../assets/img/jomalone.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Kenzo '" src="../assets/img/kenzo.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Lacoste '" src="../assets/img/lacoste.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Le Labo '" src="../assets/img/lelabo.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'L\'Occitane '" src="../assets/img/loccitane.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Maison Francis Kurkdjian '" src="../assets/img/masion.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Montana '" src="../assets/img/montana.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Penhaligon\'s '" src="../assets/img/penhaligons.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Prada '" src="../assets/img/prada.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Santa Maria Novella '" src="../assets/img/santamaria.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Serge Lutens '" src="../assets/img/serge.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Tom Ford '" src="../assets/img/tomford.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Yves Saint Laurent '" src="../assets/img/saint.png" style="width:4rem; height:2rem;">

                        </div>
                      </div>
                    </div>
                  </div>
                  <PhotoDetailModal
                    :photoData='photoData'
                    :username='username'
                     />   
                </div>
              </div>
            </div>
          </div>

          <div v-if="flag==2" class="text-center py-1" style="background-color:rgba(0,0,0,0.05);">
            <div class="py-5" v-if="summerData.length == 0">
              <p class="mb-0">아직 여름 옷이 없어요.</p>
            </div>
            <div v-else>
              <div class="row my-3 mx-1">
                <div class="col-12 col-md-4 col-lg-3 px-1 mb-3 py-1" v-for="item in summerData" :key="item.id">
                  <div class="card content" style="border:0;" data-toggle="modal" data-target="#photodetail" @click="photo(item)">
                    <div class="content-overlay">
                    </div>
                    <img class="content-image" style="width:100%;height:40vh;" :src="server_url + item.image" alt="">
                    <div class="content-details fadeIn-bottom">
                      
                      <div class="d-flex justify-content-center my-5">
                        <div class="mr-2" v-for="line in item.adjectiveList" :key="line.id">
                          <b-badge variant="light">{{line}}</b-badge>
                        </div>
                      </div>
                      <div class="d-flex justify-content-center my-2">
                        <b-badge v-if="item.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                        <div v-for="line in item.lineList" :key="line.id">
                          <b-badge v-if="line == 'floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                        </div>
                      </div>
                      <!-- <div class="d-flex justify-content-between mt-5" > -->
                        <!-- <small class="m-0 p-0" style="font-weight:bold;color:white">향수</small> -->
                        <!-- <div  class="p-1 mx-1 bg-white" v-for="perfume in item.perfumedata" :key="perfume.id">
                          <img style="width:50px;height:50px;" :src="perfume.image" alt="">
                        </div>
                      </div> -->
                      <div class="d-flex justify-content-between mt-5" >
                        <div class="mr-2" v-for="perfume in item.perfumedata" :key="perfume.id">
                          <img v-if="perfume.brand == 'Acqua di Parma '" src="../assets/img/acqua_di_parma.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Bulgari '" src="../assets/img/bulgari.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Burberry '" src="../assets/img/burberry.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Byredo '" src="../assets/img/byredo.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Calvin Klein '" src="../assets/img/calvin-klein.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Cartier '" src="../assets/img/cartier.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Chanel '" src="../assets/img/chanel.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Christian Dior '" src="../assets/img/dior.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Creed '" src="../assets/img/creed.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Demeter Fragrance Library '" src="../assets/img/demeter.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Diptyque '" src="../assets/img/diptyque.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Dolce & Gabbana '" src="../assets/img/dolce.jpg" style="width:11rem; height:2rem;">
                          <img v-if="perfume.brand == 'Editions de Parfums Frederic Malle '" src="../assets/img/frederic.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Estée Lauder '" src="../assets/img/estee.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Giorgio Armani '" src="../assets/img/giorgio.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Givenchy '" src="../assets/img/givenchy.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Gucci '" src="../assets/img/gucci.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Hermès '" src="../assets/img/hermes.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Hugo Boss '" src="../assets/img/boss.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Jo Malone London '" src="../assets/img/jomalone.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Kenzo '" src="../assets/img/kenzo.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Lacoste '" src="../assets/img/lacoste.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Le Labo '" src="../assets/img/lelabo.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'L\'Occitane '" src="../assets/img/loccitane.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Maison Francis Kurkdjian '" src="../assets/img/masion.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Montana '" src="../assets/img/montana.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Penhaligon\'s '" src="../assets/img/penhaligons.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Prada '" src="../assets/img/prada.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Santa Maria Novella '" src="../assets/img/santamaria.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Serge Lutens '" src="../assets/img/serge.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Tom Ford '" src="../assets/img/tomford.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Yves Saint Laurent '" src="../assets/img/saint.png" style="width:4rem; height:2rem;">

                        </div>
                      </div>
                    </div>
                  </div>
                  <PhotoDetailModal
                    :photoData='photoData'
                    :username='username'
                     />   
                </div>
              </div>
            </div>
          </div>

          <div v-if="flag==3" class="text-center py-1" style="background-color:rgba(0,0,0,0.05);">
            <div class="py-5" v-if="autumnData.length == 0">
              <p class="mb-0">아직 가을 옷이 없어요.</p>
            </div>
            <div v-else>
              <div class="row my-3 mx-1">
                <div class="col-12 col-md-4 col-lg-3 px-1 mb-3 py-1" v-for="item in autumnData" :key="item.id">
                  <div class="card content" style="border:0;" data-toggle="modal" data-target="#photodetail" @click="photo(item)">
                    <div class="content-overlay">
                    </div>
                    <img class="content-image" style="width:100%;height:40vh;" :src="server_url + item.image" alt="">
                    <div class="content-details fadeIn-bottom">
                      
                      <div class="d-flex justify-content-center my-5">
                        <div class="mr-2" v-for="line in item.adjectiveList" :key="line.id">
                          <b-badge variant="light">{{line}}</b-badge>
                        </div>
                      </div>
                      <div class="d-flex justify-content-center my-2">
                        <b-badge v-if="item.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                        <div v-for="line in item.lineList" :key="line.id">
                          <b-badge v-if="line == 'floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                        </div>
                      </div>
                      <div class="d-flex justify-content-between mt-5" >
                        <div class="mr-2" v-for="perfume in item.perfumedata" :key="perfume.id">
                          <img v-if="perfume.brand == 'Acqua di Parma '" src="../assets/img/acqua_di_parma.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Bulgari '" src="../assets/img/bulgari.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Burberry '" src="../assets/img/burberry.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Byredo '" src="../assets/img/byredo.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Calvin Klein '" src="../assets/img/calvin-klein.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Cartier '" src="../assets/img/cartier.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Chanel '" src="../assets/img/chanel.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Christian Dior '" src="../assets/img/dior.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Creed '" src="../assets/img/creed.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Demeter Fragrance Library '" src="../assets/img/demeter.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Diptyque '" src="../assets/img/diptyque.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Dolce & Gabbana '" src="../assets/img/dolce.jpg" style="width:11rem; height:2rem;">
                          <img v-if="perfume.brand == 'Editions de Parfums Frederic Malle '" src="../assets/img/frederic.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Estée Lauder '" src="../assets/img/estee.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Giorgio Armani '" src="../assets/img/giorgio.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Givenchy '" src="../assets/img/givenchy.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Gucci '" src="../assets/img/gucci.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Hermès '" src="../assets/img/hermes.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Hugo Boss '" src="../assets/img/boss.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Jo Malone London '" src="../assets/img/jomalone.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Kenzo '" src="../assets/img/kenzo.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Lacoste '" src="../assets/img/lacoste.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Le Labo '" src="../assets/img/lelabo.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'L\'Occitane '" src="../assets/img/loccitane.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Maison Francis Kurkdjian '" src="../assets/img/masion.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Montana '" src="../assets/img/montana.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Penhaligon\'s '" src="../assets/img/penhaligons.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Prada '" src="../assets/img/prada.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Santa Maria Novella '" src="../assets/img/santamaria.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Serge Lutens '" src="../assets/img/serge.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Tom Ford '" src="../assets/img/tomford.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Yves Saint Laurent '" src="../assets/img/saint.png" style="width:4rem; height:2rem;">
                        </div>
                      </div>
                    </div>
                  </div>
                  <PhotoDetailModal
                    :photoData='photoData'
                    :username='username'
                    @deleteClothes='deleteClothes'
                     />   
                </div>
              </div>
            </div>
          </div>

          <div v-if="flag==4" class="text-center py-1" style="background-color:rgba(0,0,0,0.05);">
            <div class="py-5" v-if="winterData.length == 0">
              <p class="mb-0">아직 겨울 옷이 없어요.</p>
            </div>
            <div v-else>
              <div class="row my-3 mx-1">
                <div class="col-12 col-md-4 col-lg-3 px-1 mb-3 py-1" v-for="item in winterData" :key="item.id">
                  <div class="card content" style="border:0;" data-toggle="modal" data-target="#photodetail" @click="photo(item)">
                    <div class="content-overlay">
                    </div>
                    <img class="content-image" style="width:100%;height:40vh;" :src="server_url + item.image" alt="">
                    <div class="content-details fadeIn-bottom">
                      
                      <div class="d-flex justify-content-center my-5">
                        <div class="mr-2" v-for="line in item.adjectiveList" :key="line.id">
                          <b-badge variant="light">{{line}}</b-badge>
                        </div>
                      </div>
                      <div class="d-flex justify-content-center my-2">
                        <b-badge v-if="item.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                        <div v-for="line in item.lineList" :key="line.id">
                          <b-badge v-if="line == 'floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                          <b-badge v-if="line == 'cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                        </div>
                      </div>
                      <!-- <div class="d-flex justify-content-between mt-5" > -->
                        <!-- <small class="m-0 p-0" style="font-weight:bold;color:white">향수</small> -->
                        <!-- <div  class="p-1 mx-1 bg-white" v-for="perfume in item.perfumedata" :key="perfume.id">
                          <img style="width:50px;height:50px;" :src="perfume.image" alt="">
                        </div>
                      </div> -->
                      <div class="d-flex justify-content-between mt-5" >
                        <div class="mr-2" v-for="perfume in item.perfumedata" :key="perfume.id">
                          <img v-if="perfume.brand == 'Acqua di Parma '" src="../assets/img/acqua_di_parma.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Bulgari '" src="../assets/img/bulgari.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Burberry '" src="../assets/img/burberry.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Byredo '" src="../assets/img/byredo.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Calvin Klein '" src="../assets/img/calvin-klein.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Cartier '" src="../assets/img/cartier.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Chanel '" src="../assets/img/chanel.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Christian Dior '" src="../assets/img/dior.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Creed '" src="../assets/img/creed.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Demeter Fragrance Library '" src="../assets/img/demeter.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Diptyque '" src="../assets/img/diptyque.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Dolce & Gabbana '" src="../assets/img/dolce.jpg" style="width:11rem; height:2rem;">
                          <img v-if="perfume.brand == 'Editions de Parfums Frederic Malle '" src="../assets/img/frederic.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Estée Lauder '" src="../assets/img/estee.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Giorgio Armani '" src="../assets/img/giorgio.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Givenchy '" src="../assets/img/givenchy.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Gucci '" src="../assets/img/gucci.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Hermès '" src="../assets/img/hermes.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Hugo Boss '" src="../assets/img/boss.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Jo Malone London '" src="../assets/img/jomalone.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Kenzo '" src="../assets/img/kenzo.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Lacoste '" src="../assets/img/lacoste.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Le Labo '" src="../assets/img/lelabo.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'L\'Occitane '" src="../assets/img/loccitane.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Maison Francis Kurkdjian '" src="../assets/img/masion.jpg" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Montana '" src="../assets/img/montana.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Penhaligon\'s '" src="../assets/img/penhaligons.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Prada '" src="../assets/img/prada.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Santa Maria Novella '" src="../assets/img/santamaria.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Serge Lutens '" src="../assets/img/serge.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Tom Ford '" src="../assets/img/tomford.png" style="width:4rem; height:2rem;">
                          <img v-if="perfume.brand == 'Yves Saint Laurent '" src="../assets/img/saint.png" style="width:4rem; height:2rem;">

                        </div>
                      </div>
                    </div>
                  </div>
                  
                  <PhotoDetailModal
                    :photoData='photoData'
                    :username='username'
                     />   
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import axios from "axios";
import constants from '../lib/constants'
import PhotoDetailModal from '../components/main/PhotoDetailModal.vue'

export default {
  name: "Profile",
  components:{
    PhotoDetailModal
  },
  data: () => {
    return {
      profileData: {},
      reviewData: {},
      springData:{},
      summerData:{},
      autumnData:{},
      winterData:{},
      flag : 0,
      username:'',
      server_url : constants.SERVER_URL,
      photoData:{}
    };
  },
  created() {
      this.getProfile()
  },
  methods: {
      getProfile() {
       if (this.$cookies.isKey("auth-token")){
            axios.get(constants.SERVER_URL + `/api/accounts/userdetail/${this.$cookies.get('email')}/`)
            .then((res) => {
            this.profileData = res.data
            this.getReview()
            })
            .catch((err)=>{
            console.log(err);
            })
       } else{
           this.$router.push({name:constants.URL_TYPE.MAIN})
       }
    },
    logout() {
        const axiosConfig ={
          headers:{
            Authorization : `Token ${this.$cookies.get('auth-token')}`
          },
        }
        axios.post(constants.SERVER_URL + '/api/rest-auth/logout/',null,axiosConfig)
        .then(()=>{
        this.$cookies.remove('auth-token')
        this.isLoggedIn=false
        this.$router.go()
        this.$router.push({name:constants.URL_TYPE.MAIN})
        })
        .catch((error)=>{
            console.log(error.response.data)
        })
    },
    getReview() {
        axios.get(constants.SERVER_URL + '/api/accounts/clothes/')
        .then((res) => {
            this.reviewData=res.data.data.filter(item => item.user == this.profileData.id )
            this.springData=this.reviewData.filter(item => item.created_at.substring(5,7) == '03' || item.created_at.substring(5,7) == '04' || item.created_at.substring(5,7) == '05' )
            this.summerData=this.reviewData.filter(item => item.created_at.substring(5,7) == '06' || item.created_at.substring(5,7) == '07' || item.created_at.substring(5,7) == '08' )
            this.autumnData=this.reviewData.filter(item => item.created_at.substring(5,7) == '09' || item.created_at.substring(5,7) == '10' || item.created_at.substring(5,7) == '11' )
            this.winterData=this.reviewData.filter(item => item.created_at.substring(5,7) == '12' || item.created_at.substring(5,7) == '01' || item.created_at.substring(5,7) == '02' )
        })
    },
    giveFlag(num){
      if (this.flag == num) {
        this.flag = 0
      } else {
        this.flag = num
      }
    },
    photo(data) {
        this.photoData = data
        this.username = this.profileData.id
    },
    deleteClothes(id) {
        const axiosConfig ={
          headers:{
              Authorization : `Token ${this.$cookies.get('auth-token')}`
              },
        }
        axios
        .delete(constants.SERVER_URL + `/api/accounts/clothes/${id}/`,null,axiosConfig)
        .then(() => {
          this.$router.go()
        })
        .catch((err) => {
            console.log(err);
        });
    },
  },
};
</script>

<style scoped>
.content {
    position: relative;
    width: 90%;
    max-width: 400px;
    margin: auto;
    overflow: hidden
}

.content .content-overlay {
  background: rgba(255,255,255, 0.7);
  position: absolute;
  height: 100%;
  width: 100%;
  left: 0;
  top: 0;
  bottom: 0;
  right: 0;
  opacity: 0;
  -webkit-transition: all 0.4s ease-in-out 0s;
  -moz-transition: all 0.4s ease-in-out 0s;
  transition: all 0.4s ease-in-out 0s
}

.content:hover .content-overlay {
  opacity: 1
}

.content-image {
  width: 100%
}

.content-details {
    position: absolute;
    text-align: center;
    padding-left: 1em;
    padding-right: 1em;
    width: 100%;
    top: 50%;
    left: 50%;
    opacity: 0;
    -webkit-transform: translate(-50%, -50%);
    -moz-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    -webkit-transition: all 0.3s ease-in-out 0s;
    -moz-transition: all 0.3s ease-in-out 0s;
    transition: all 0.3s ease-in-out 0s
}

.content:hover .content-details {
  top: 50%;
  left: 50%;
  opacity: 1
}

.fadeIn-bottom {
    top: 80%
}
</style>