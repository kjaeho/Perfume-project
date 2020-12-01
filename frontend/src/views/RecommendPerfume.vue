<template>
  <div>
    <div class="container col-md-10 mt-5" style="margin-left:10%;">
        <div class="d-flex">
            <div>
                <span class="my-auto ml-3" style="color:pink; font-size:3rem; font-weight:bold;">{{username}}</span>
                <span class="ml-2" style="font-size:1.5rem; font-weight:bold; ">님에게 추천드리는 향수 :)</span>
            </div>
            <!-- <div style="cursor:pointer;" @click="goMain()" class="mt-auto ml-auto">
                <b-icon icon="box-arrow-in-left" font-scale="2.5"></b-icon>
            </div> -->
        </div>

        <!-- <div class="card border"> -->
        <div class="row text-center p-4" style="cursor:pointer;">
          <div class="col" @click="giveFlag(0)">
            <img style="width:45px;" src="data:image/svg+xml;base64,PHN2ZyBpZD0iRmlsbGVkX3N0cm9rZV9jdXR0aW5nX2V4X1JldmlzZSIgaGVpZ2h0PSI1MTIiIHZpZXdCb3g9IjAgMCA1MTIgNTEyIiB3aWR0aD0iNTEyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGRhdGEtbmFtZT0iRmlsbGVkIHN0cm9rZSBjdXR0aW5nIGV4IFJldmlzZSI+PGc+PHBhdGggZD0ibTM0NCA1NmgxMjh2NDAwaC0xMjh6IiBmaWxsPSIjZmFhMjMxIiB0cmFuc2Zvcm09Im1hdHJpeCgtMSAwIDAgLTEgODE2IDUxMikiLz48cGF0aCBkPSJtMzI4IDI0aDE2MHYzMmgtMTYweiIgZmlsbD0iI2I4YjhiOCIgdHJhbnNmb3JtPSJtYXRyaXgoLTEgMCAwIC0xIDgxNiA4MCkiLz48cGF0aCBkPSJtNDI0IDgwaDE2djg4aC0xNnoiLz48cGF0aCBkPSJtNDI0IDE4NGgxNnY4OGgtMTZ6Ii8+PHBhdGggZD0ibTM3NiA4MGgxNnY0OGgtMTZ6Ii8+PHBhdGggZD0ibTQ4OCA0NTZ2LTY0YTI0IDI0IDAgMCAwIC0yNC0yNGgtMTZhMjQgMjQgMCAwIDAgLTI0IDI0djY0eiIgZmlsbD0iIzYzYzUyMSIvPjxwYXRoIGQ9Im0zOTIgNDE2aDY0YTAgMCAwIDAgMSAwIDB2MTBhMzAgMzAgMCAwIDEgLTMwIDMwaC00YTMwIDMwIDAgMCAxIC0zMC0zMHYtMTBhMCAwIDAgMCAxIDAgMHoiIGZpbGw9IiM5ZmRjNmUiIHRyYW5zZm9ybT0ibWF0cml4KC0xIDAgMCAtMSA4NDggODcyKSIvPjxwYXRoIGQ9Im00MCA1NmgxMjh2NDAwaC0xMjh6IiBmaWxsPSIjZmFhMjMxIi8+PHBhdGggZD0ibTM5MiA0NTZoLTI3MnYtMjg4bDEzNi04OCAxMzYgODh6IiBmaWxsPSIjZmFjODUwIi8+PHBhdGggZD0ibTEyMCAyODhoMjcydjMyaC0yNzJ6IiBmaWxsPSIjYjhiOGI4Ii8+PHBhdGggZD0ibTI0IDQ1Nmg0NjR2MzJoLTQ2NHoiIGZpbGw9IiM0ZDRkNGQiLz48ZyBmaWxsPSIjZmZmZGZhIj48cGF0aCBkPSJtMjU2IDM1MmEyNCAyNCAwIDAgMSAyNCAyNHY4MGEwIDAgMCAwIDEgMCAwaC00OGEwIDAgMCAwIDEgMCAwdi04MGEyNCAyNCAwIDAgMSAyNC0yNHoiLz48cGF0aCBkPSJtMTc2IDM1MmEyNCAyNCAwIDAgMSAyNCAyNHY4MGEwIDAgMCAwIDEgMCAwaC00OGEwIDAgMCAwIDEgMCAwdi04MGEyNCAyNCAwIDAgMSAyNC0yNHoiLz48cGF0aCBkPSJtMzM2IDM1MmEyNCAyNCAwIDAgMSAyNCAyNHY4MGEwIDAgMCAwIDEgMCAwaC00OGEwIDAgMCAwIDEgMCAwdi04MGEyNCAyNCAwIDAgMSAyNC0yNHoiLz48cGF0aCBkPSJtMjU2IDE0NGEzMiAzMiAwIDAgMSAzMiAzMnYxMTJhMCAwIDAgMCAxIDAgMGgtNjRhMCAwIDAgMCAxIDAgMHYtMTEyYTMyIDMyIDAgMCAxIDMyLTMyeiIvPjxwYXRoIGQ9Im0xNzIgMTg0YTIwIDIwIDAgMCAxIDIwIDIwdjg0YTAgMCAwIDAgMSAwIDBoLTQwYTAgMCAwIDAgMSAwIDB2LTg0YTIwIDIwIDAgMCAxIDIwLTIweiIvPjxwYXRoIGQ9Im0zNDAgMTg0YTIwIDIwIDAgMCAxIDIwIDIwdjg0YTAgMCAwIDAgMSAwIDBoLTQwYTAgMCAwIDAgMSAwIDB2LTg0YTIwIDIwIDAgMCAxIDIwLTIweiIvPjwvZz48cGF0aCBkPSJtMjQgMjRoMTYwdjMyaC0xNjB6IiBmaWxsPSIjYjhiOGI4Ii8+PHBhdGggZD0ibTE4NCA2NGgtMTYwYTggOCAwIDAgMSAtOC04di0zMmE4IDggMCAwIDEgOC04aDE2MGE4IDggMCAwIDEgOCA4djMyYTggOCAwIDAgMSAtOCA4em0tMTUyLTE2aDE0NHYtMTZoLTE0NHoiLz48cGF0aCBkPSJtNzIgODBoMTZ2ODhoLTE2eiIvPjxwYXRoIGQ9Im03MiAxODRoMTZ2ODhoLTE2eiIvPjxwYXRoIGQ9Im0xMjAgODBoMTZ2NDhoLTE2eiIvPjxwYXRoIGQ9Im0yNCA0NTZ2LTY0YTI0IDI0IDAgMCAxIDI0LTI0aDE2YTI0IDI0IDAgMCAxIDI0IDI0djY0eiIgZmlsbD0iIzYzYzUyMSIvPjxwYXRoIGQ9Im04NiA0MTZoNGEzMCAzMCAwIDAgMSAzMCAzMHYxMGEwIDAgMCAwIDEgMCAwaC02NGEwIDAgMCAwIDEgMCAwdi0xMGEzMCAzMCAwIDAgMSAzMC0zMHoiIGZpbGw9IiM5ZmRjNmUiLz48cGF0aCBkPSJtNDg4IDY0YTggOCAwIDAgMCA4LTh2LTMyYTggOCAwIDAgMCAtOC04aC0xNjBhOCA4IDAgMCAwIC04IDh2MzJhOCA4IDAgMCAwIDggOGg4djU4LjIzNmwtNzUuNjU0LTQ4Ljk1M2E4IDggMCAwIDAgLTguNjkyIDBsLTc1LjY1NCA0OC45NTN2LTU4LjIzNmg4YTggOCAwIDAgMCA4LTh2LTMyYTggOCAwIDAgMCAtOC04aC0xNjBhOCA4IDAgMCAwIC04IDh2MzJhOCA4IDAgMCAwIDggOGg4djEwNGgxNnYtMTA0aDExMnY2OC41ODlsLTQ0LjM0NiAyOC42OTRhOCA4IDAgMCAwIC0zLjY1NCA2LjcxN3YyNDcuMDMyYTM3LjggMzcuOCAwIDAgMCAtMTYtNi41NTh2LTE2LjQ3NGEzMS44NjkgMzEuODY5IDAgMCAwIC04LTIxLjE0NHYtODIuODU2aC0xNnY3My4wMTJhMzEuOTg2IDMxLjk4NiAwIDAgMCAtOC0xLjAxMmgtMTZ2LTE3NmgtMTZ2MTgwLjNhMzIuMDE5IDMyLjAxOSAwIDAgMCAtMTYgMjcuN3Y5NmE4IDggMCAwIDAgOCA4aDQ2NGE4IDggMCAwIDAgOC04di05NmEzMi4wMTkgMzIuMDE5IDAgMCAwIC0xNi0yNy43di0zMDAuM3ptLTQ1Ni0zMmgxNDR2MTZoLTE0NHptMzA0IDBoMTQ0djE2aC0xNDR6bS04MCA1Ny41MjkgMTI4IDgyLjgyM3YxMDcuNjQ4aC0xNnYtNzZhMjggMjggMCAwIDAgLTU2IDB2NzZoLTE2di0xMDRhNDAgNDAgMCAwIDAgLTgwIDB2MTA0aC0xNnYtNzZhMjggMjggMCAwIDAgLTU2IDB2NzZoLTE2di0xMDcuNjQ4em0yMjQgMzAyLjQ3MXY1NmgtMTZ2LTJhMzguMDYxIDM4LjA2MSAwIDAgMCAtMzItMzcuNTI2di0xNi40NzRhMTYuMDE5IDE2LjAxOSAwIDAgMSAxNi0xNmgxNmExNi4wMTkgMTYuMDE5IDAgMCAxIDE2IDE2em0tNTggMzJoNGEyMi4wMjUgMjIuMDI1IDAgMCAxIDIyIDIydjJoLTQ4di0yYTIyLjAyNSAyMi4wMjUgMCAwIDEgMjItMjJ6bS0zOCAyNGgtMTZ2LTcyYTMyIDMyIDAgMCAwIC02NCAwdjcyaC0xNnYtNzJhMzIgMzIgMCAwIDAgLTY0IDB2NzJoLTE2di03MmEzMiAzMiAwIDAgMCAtNjQgMHY3MmgtMTZ2LTEyMGgxNjh2LTE2aC0xNjh2LTE2aDI1NnYxNmgtNzJ2MTZoNzJ6bS0zMiAwaC0zMnYtNzJhMTYgMTYgMCAwIDEgMzIgMHptLTgwIDBoLTMydi03MmExNiAxNiAwIDAgMSAzMiAwem0tODAgMGgtMzJ2LTcyYTE2IDE2IDAgMCAxIDMyIDB6bS04LTE2OGgtMjR2LTc2YTEyIDEyIDAgMCAxIDI0IDB6bTk2IDBoLTQ4di0xMDRhMjQgMjQgMCAwIDEgNDggMHptNzIgMGgtMjR2LTc2YTEyIDEyIDAgMCAxIDI0IDB6bS0yNDAgMTY2djJoLTQ4di0yYTIyLjAyNSAyMi4wMjUgMCAwIDEgMjItMjJoNGEyMi4wMjUgMjIuMDI1IDAgMCAxIDIyIDIyem0tNjQtNzBoMTZhMTYuMDE5IDE2LjAxOSAwIDAgMSAxNiAxNnYxNi40NzRhMzguMDYxIDM4LjA2MSAwIDAgMCAtMzIgMzcuNTI2djJoLTE2di01NmExNi4wMTkgMTYuMDE5IDAgMCAxIDE2LTE2em00MzIgMTA0aC00NDh2LTE2aDQ0OHptLTE2LTEyMGgtMTZhMzEuOTg2IDMxLjk4NiAwIDAgMCAtOCAxLjAxMnYtNzMuMDEyaC0xNnY4Mi44NTZhMzEuODY5IDMxLjg2OSAwIDAgMCAtOCAyMS4xNDR2MTYuNDc0YTM3LjggMzcuOCAwIDAgMCAtMTYgNi41NTh2LTI0Ny4wMzJhOCA4IDAgMCAwIC0zLjY1NC02LjcxN2wtNDQuMzQ2LTI4LjY5NHYtNjguNTg5aDExMnoiLz48L2c+PC9zdmc+" />
            <p class="mb-0 font-weight-bold mt-1" style="color:hotpink;">대학생</p>
          </div>
          <div class="col" @click="giveFlag(2)">
            <img style="width:45px;" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pg0KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjAuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPg0KPHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJDYXBhXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4Ig0KCSB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgNTEyIDUxMjsiIHhtbDpzcGFjZT0icHJlc2VydmUiPg0KPGc+DQoJPHBhdGggc3R5bGU9ImZpbGw6IzQxNEI4MjsiIGQ9Ik0zMjkuOTE1LDQ5OC40MjhjLTEwLjcyNC0yLjM3OC0xNy40OS0xMi45OTktMTUuMTExLTIzLjcyM2wxNy40MzItNzguNjA2bC0yNy45NTEtNjYuMTM5DQoJCWMtNC4yNzYtMTAuMTE5LDAuNDYtMjEuNzg3LDEwLjU3OC0yNi4wNjJjMTAuMTE3LTQuMjc1LDIxLjc4NiwwLjQ2LDI2LjA2MiwxMC41NzhsMzAuNDIxLDcxLjk4OA0KCQljMS42MDgsMy44MDQsMS45OTEsOC4wMTYsMS4wOTcsMTIuMDQ4bC0xOC44MDcsODQuODA1QzM1MS4yNjcsNDk0LjAxMSwzNDAuNjY1LDUwMC44MTMsMzI5LjkxNSw0OTguNDI4eiIvPg0KCTxwYXRoIHN0eWxlPSJmaWxsOiM0MTRCODI7IiBkPSJNMjgwLjIwMSw1MTJjLTExLjAzMiwwLTE5Ljk3NS04Ljk0My0xOS45NzUtMTkuOTc1VjMzMi4zNjJjMC0xMS4wMzIsOC45NDMtMTkuOTc1LDE5Ljk3NS0xOS45NzUNCgkJYzExLjAzMiwwLDE5Ljk3NSw4Ljk0MywxOS45NzUsMTkuOTc1djE1OS42NjNDMzAwLjE3Niw1MDMuMDU3LDI5MS4yMzMsNTEyLDI4MC4yMDEsNTEyeiIvPg0KPC9nPg0KPHBhdGggc3R5bGU9ImZpbGw6IzI1MkQ1QzsiIGQ9Ik0yNzUuNTg3LDE3Mi40NzZsLTU3LjEzOC0xOC44MTdsLTM2LjEwNi01OC4zODRjLTQuODE1LTcuNzg1LTE1LjAyOC0xMC4xOTMtMjIuODE1LTUuMzc5DQoJYy03Ljc4NSw0LjgxNS0xMC4xOTMsMTUuMDI5LTUuMzc4LDIyLjgxNWwzOS4yODQsNjMuNTIzYzIuMDUzLDMuMzIsNS4yMTEsNS44MDgsOC45MTksNy4wMjdsNTcuODczLDE5LjAzM3YxMzAuMDY3aDQ0LjA4NWg0NC4wODUNCglWMTcyLjQ4QzI5OS42OTUsMTcyLjQ2MiwzMzMuODg2LDE3Mi41MzUsMjc1LjU4NywxNzIuNDc2eiIvPg0KPHBhdGggc3R5bGU9ImZpbGw6IzFCMjI0QTsiIGQ9Ik00NDAuOTcsNDguMjEyYy04LjExNC00LjIzMy0xOC4xMjYtMS4wOS0yMi4zNjIsNy4wMjVsLTQyLjAwNCw4MC40ODRsLTQ2LjI2MywzNi43NTVoLTE3LjA3OWgtOC45NQ0KCXYxNTkuODg1aDQ0LjA4NVYyMDAuNDY4bDUxLjU4My00MC45ODFjMS44MTYtMS40NDMsMy4zMS0zLjI1Miw0LjM4NC01LjMwOWw0My42MzItODMuNjA0DQoJQzQ1Mi4yMzEsNjIuNDU5LDQ0OS4wODUsNTIuNDQ3LDQ0MC45Nyw0OC4yMTJ6Ii8+DQo8Y2lyY2xlIHN0eWxlPSJmaWxsOiNCQTY3NDY7IiBjeD0iMzA0LjMwMyIgY3k9IjEyNy4zNTkiIHI9IjM0LjQ5OSIvPg0KPHBvbHlnb24gc3R5bGU9ImZpbGw6I0ZGRkZGRjsiIHBvaW50cz0iMjc4LjkwNywxNzIuNDc2IDMwNC4zMDksMjM5LjEzNSAzMjkuNzEsMTcyLjQ3NiAiLz4NCjxwYXRoIHN0eWxlPSJmaWxsOiNGRjNDM0M7IiBkPSJNMzE2LjA2OSwxOTkuOTIyYzAuMzE3LTEuNTg3LDAuMDY0LTMuMjM0LTAuNzE1LTQuNjUxbC01LjY3LTEwLjMxM2w0Ljg5MS04Ljg5NQ0KCWMwLjg4NS0xLjYwOC0wLjI4MS0zLjU4Ny0yLjExOS0zLjU4N2gtMTYuMzAyYy0xLjgzNSwwLTMuMDA0LDEuOTc3LTIuMTE5LDMuNTg3bDQuOTA3LDguOTI1bC01LjY1NSwxMC4yODQNCgljLTAuNzc5LDEuNDE3LTEuMDMyLDMuMDYzLTAuNzE2LDQuNjQ5bDMuNTMzLDE3LjY4MWw4LjIwNiwyMS41MzNsOC4yMzUtMjEuNjFMMzE2LjA2OSwxOTkuOTIyeiIvPg0KPGc+DQoJPHBhdGggc3R5bGU9ImZpbGw6I0ZGRkZGRjsiIGQ9Ik0xNTcuNzg4LDExOC41OTRsMjguNDM4LTE3LjAzN2wtMy44ODMtNi4yOGMtNC44MTUtNy43ODYtMTUuMDI4LTEwLjE5My0yMi44MTUtNS4zNzkNCgkJYy03Ljc4NSw0LjgxNS0xMC4xOTMsMTUuMDI4LTUuMzc4LDIyLjgxNUwxNTcuNzg4LDExOC41OTR6Ii8+DQoJPHBhdGggc3R5bGU9ImZpbGw6I0ZGRkZGRjsiIGQ9Ik00NDQuNTM4LDc3LjE5OGwzLjQ1Ny02LjYyNGM0LjIzNS04LjExNiwxLjA5LTE4LjEyNy03LjAyNS0yMi4zNjINCgkJYy04LjExNC00LjIzMy0xOC4xMjYtMS4wOS0yMi4zNjIsNy4wMjVsLTMuNDA2LDYuNTI3TDQ0NC41MzgsNzcuMTk4eiIvPg0KPC9nPg0KPGc+DQoJPHBhdGggc3R5bGU9ImZpbGw6I0JBNjc0NjsiIGQ9Ik0xODIuMzQzLDk1LjI3N2MtNC44MTUtNy43ODYtMTUuMDI4LTEwLjE5My0yMi44MTUtNS4zNzljLTcuNzg1LDQuODE1LTEwLjE5MywxNS4wMjgtNS4zNzgsMjIuODE1DQoJCUwxODIuMzQzLDk1LjI3N3oiLz4NCgk8cGF0aCBzdHlsZT0iZmlsbDojQkE2NzQ2OyIgZD0iTTQ0Ny45OTUsNzAuNTczYzQuMjM1LTguMTE2LDEuMDktMTguMTI3LTcuMDI1LTIyLjM2MmMtOC4xMTQtNC4yMzMtMTguMTI2LTEuMDktMjIuMzYyLDcuMDI1DQoJCUw0NDcuOTk1LDcwLjU3M3oiLz4NCjwvZz4NCjxwYXRoIHN0eWxlPSJmaWxsOiM1OTI1MEY7IiBkPSJNMTUxLjY2MSwxMjMuNTE4Yy0xLjg3LDAtMy43MzktMC43MjYtNS4xNDUtMi4xNzNsLTI0LjY4OS0yNS4zOGMtMS4zMjgtMS4zNjUtMi4wNTktMy4yLTIuMDMyLTUuMTAzDQoJYzAuMDI2LTEuOTAzLDAuODA4LTMuNzE5LDIuMTczLTUuMDQ1bDI2LjQwOS0yNS42ODljMi44NDEtMi43NjQsNy4zODUtMi43MDEsMTAuMTQ4LDAuMTQxbDI0LjY4OSwyNS4zOA0KCWMxLjMyOCwxLjM2NSwyLjA1OSwzLjIsMi4wMzIsNS4xMDNjLTAuMDI3LDEuOTAzLTAuODA4LDMuNzE5LTIuMTczLDUuMDQ1bC0yNi40MDksMjUuNjg5DQoJQzE1NS4yNywxMjIuODQyLDE1My40NjQsMTIzLjUxOCwxNTEuNjYxLDEyMy41MTh6IE0xMzcuMTIxLDkxLjEwMWwxNC42OCwxNS4wOTFsMTYuMTItMTUuNjhsLTE0LjY4LTE1LjA5MUwxMzcuMTIxLDkxLjEwMXoiLz4NCjxwYXRoIHN0eWxlPSJmaWxsOiM4MDM5MUI7IiBkPSJNMTA2LjUyLDEyNC43N0w2NS4wMDQsODIuMDkyYy0zLjkyMS00LjAzMi0zLjgzMi0xMC40NzksMC4xOTktMTQuNGw2Ni42MjUtNjQuODA5DQoJYzQuMDMyLTMuOTIxLDEwLjQ3OS0zLjgzMiwxNC40LDAuMTk4bDQxLjUxNCw0Mi42NzhjMy45MjEsNC4wMzIsMy44MzIsMTAuNDc5LTAuMTk5LDE0LjRsLTY2LjYyNCw2NC44MDgNCglDMTE2Ljg4OCwxMjguODksMTEwLjQ0MSwxMjguODAxLDEwNi41MiwxMjQuNzd6Ii8+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8L3N2Zz4NCg==" />
            <p class="mb-0 font-weight-bold mt-1" style="color:skyBlue;">사회초년생</p>
          </div>
          <div class="col" @click="giveFlag(3)">
            <img style="width:45px;" src="data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjUxMiIgdmlld0JveD0iMCAwIDUxMiA1MTIiIHdpZHRoPSI1MTIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgaWQ9IkZsYXQiPjxwYXRoIGQ9Im0zNzQuNCA0My4yYTQ4IDQ4IDAgMCAxIDkuNiAyOC44djM3LjA4OGEyNi4zNDIgMjYuMzQyIDAgMCAwIDcuNzE2IDE4LjYyOCAyOC4yODQgMjguMjg0IDAgMCAxIDguMjg0IDIwIDI4LjI4NCAyOC4yODQgMCAwIDEgLTI4LjI4NCAyOC4yODRoLTEwMy40MzJhMjguMjg0IDI4LjI4NCAwIDAgMSAtMjguMjg0LTI4LjI4NCAyOC4yODQgMjguMjg0IDAgMCAxIDguMjg0LTIwIDI2LjM0MiAyNi4zNDIgMCAwIDAgNy43MTYtMTguNjI4di0zNy4wODhhNDggNDggMCAwIDEgOS42LTI4LjggNDcuOTkyIDQ3Ljk5MiAwIDAgMSAzOC40LTE5LjJoMzJhNDcuOTkyIDQ3Ljk5MiAwIDAgMSAzOC40IDE5LjJ6IiBmaWxsPSIjYmZiZmJkIi8+PHBhdGggZD0ibTM2OCAxMjBhNDggNDggMCAwIDEgLTQ4IDQ4IDQ4LjUyNiA0OC41MjYgMCAwIDEgLTEwLjg2LTEuMjMgNDguMDQ1IDQ4LjA0NSAwIDAgMSAtMzcuMTQtNDYuNzd2LTQwYTUxLjc2NiA1MS43NjYgMCAwIDAgNDYuMzEtMjguNjJsMS42OS0zLjM4Yy43MiAwIDEuNDQuMDMgMi4xNS4wOWEyNy4xMDkgMjcuMTA5IDAgMCAxIDI0Ljk2IDI2Ljk2IDI3LjcxMSAyNy43MTEgMCAwIDEgLS4zNyA0LjUxbC0xLjY3IDEwLjA0YTI2LjEgMjYuMSAwIDAgMCAxNy42MyAyOS4xMSA0MS41MyA0MS41MyAwIDAgMCA1LjMgMS4yOXoiIGZpbGw9IiNmZWM5YTMiLz48cGF0aCBkPSJtMzY4IDEyMGE0OCA0OCAwIDAgMSAtNDggNDggNDguNTI2IDQ4LjUyNiAwIDAgMSAtMTAuODYtMS4yMyA3MS43NiA3MS43NiAwIDAgMCAyMi4wMS01MS44MXYtMzJhNzEuNTY2IDcxLjU2NiAwIDAgMCAtOS0zNC44NyAyNy4xMDkgMjcuMTA5IDAgMCAxIDI0Ljk2IDI2Ljk2IDI3LjcxMSAyNy43MTEgMCAwIDEgLS4zNyA0LjUxbC0xLjY3IDEwLjA0YTI2LjEgMjYuMSAwIDAgMCAxNy42MyAyOS4xMSA0MS41MyA0MS41MyAwIDAgMCA1LjMgMS4yOXoiIGZpbGw9IiNmZWMwOTMiLz48cGF0aCBkPSJtMzkyIDIwOHYxMzZoLTEzNnYtMTM2YTMyIDMyIDAgMCAxIDMyLTMyaDcyYTMxLjk4MSAzMS45ODEgMCAwIDEgMzIgMzJ6IiBmaWxsPSIjZDM2NjlhIi8+PHBhdGggZD0ibTM5MiAyMDh2MTM2aC0xMzZ2LTY1LjUyYTM0MS4xNjMgMzQxLjE2MyAwIDAgMCAxMTcuMzctOTkuNTYgMzIuMDEgMzIuMDEgMCAwIDEgMTguNjMgMjkuMDh6IiBmaWxsPSIjY2M2Mzk1Ii8+PHBhdGggZD0ibTI0MCA3MnYzMmE0Ny45NzkgNDcuOTc5IDAgMCAxIC00NyA0Ny45OGMtLjMzLjAyLS42Ny4wMi0xIC4wMmE0OCA0OCAwIDAgMSAtNDgtNDh2LTMyYTQ4IDQ4IDAgMCAxIDk2IDB6IiBmaWxsPSIjZmVjOWEzIi8+PHBhdGggZD0ibTI0MCA3MnYzMmE0Ny45NzkgNDcuOTc5IDAgMCAxIC00NyA0Ny45OCA3MS41NTYgNzEuNTU2IDAgMCAwIDEyLjE1LTQwLjAydi0zMmE3MS43NzUgNzEuNzc1IDAgMCAwIC0yMS4wOS01MC45MXEtMS44Ni0xLjg2LTMuODYtMy41OWE0OC4wMTggNDguMDE4IDAgMCAxIDU5LjggNDYuNTR6IiBmaWxsPSIjZmVjMDkzIi8+PGcgZmlsbD0iIzdhNDMyYSI+PHBhdGggZD0ibTI5NiA5NmgxNnYxNmgtMTZ6Ii8+PHBhdGggZD0ibTMyOCA5NmgxNnYxNmgtMTZ6Ii8+PHBhdGggZD0ibTE2OCA4OGgxNnYxNmgtMTZ6Ii8+PHBhdGggZD0ibTIwMCA4OGgxNnYxNmgtMTZ6Ii8+PC9nPjxwYXRoIGQ9Im0xNDQgMTA0IDE0LjQ3MiAxNC40NzJhMTguNyAxOC43IDAgMCAwIDIxLjU4IDMuNSAxOC43IDE4LjcgMCAwIDEgOC4zNjEtMS45NzJoNy4xNzRhMTguNyAxOC43IDAgMCAxIDguMzYxIDEuOTc0IDE4LjcgMTguNyAwIDAgMCAyMS41OC0zLjVsMTQuNDcyLTE0LjQ3NHY0MGEzMiAzMiAwIDAgMSAtMzIgMzJoLTMyYTMyIDMyIDAgMCAxIC0zMi0zMnoiIGZpbGw9IiM5MjU2M2EiLz48cGF0aCBkPSJtMTQ0IDczLjExNGExNy4xMTQgMTcuMTE0IDAgMCAxIDE3LjExNC0xNy4xMTRoMi44NDZhMTcuMTEzIDE3LjExMyAwIDAgMSA3LjY1MyAxLjgwN2w4Ljc3NCA0LjM4NmExNy4xMTMgMTcuMTEzIDAgMCAwIDcuNjUzIDEuODA3aDguNTg4YTE3LjEgMTcuMSAwIDAgMCA2LjQ5Mi0xLjI3OWwxMy4yOC01LjQ0MmExNy4xIDE3LjEgMCAwIDEgNi40ODYtMS4yNzkgMTcuMTE0IDE3LjExNCAwIDAgMSAxNy4xMTQgMTcuMTE0di0xNC42OTJhMzQuNDIzIDM0LjQyMyAwIDAgMCAtMTUuMzI4LTI4LjY0MSAzNC40MjggMzQuNDI4IDAgMCAwIC0xOS4wOTQtNS43ODFoLTI3LjE1NmEzNC40MjggMzQuNDI4IDAgMCAwIC0xOS4wOTQgNS43ODEgMzQuNDIzIDM0LjQyMyAwIDAgMCAtMTUuMzI4IDI4LjY0MXoiIGZpbGw9IiM5MjU2M2EiLz48cGF0aCBkPSJtMjU2IDIwOHYxMzZoLTEzNnYtMTM2YTMyIDMyIDAgMCAxIDMyLTMyaDcyYTMxLjk1OCAzMS45NTggMCAwIDEgMzIgMzJ6IiBmaWxsPSIjZjM1MjQ0Ii8+PHBhdGggZD0ibTI1NiAyMDh2MTM2aC0xMzZ2LTg2LjJhMzQyLjUzMiAzNDIuNTMyIDAgMCAwIDExNS4xNy03OS44IDMyLjAyNyAzMi4wMjcgMCAwIDEgMjAuODMgMzB6IiBmaWxsPSIjZTY0ZDQwIi8+PHBhdGggZD0ibTEyMCAzNDRoMTM2djE0NGgtMTM2eiIgZmlsbD0iI2YzNTI0NCIvPjxwYXRoIGQ9Im0xNTIgMzA0djEzNmgtODh2LTExMmgtNDB2LTI0YTQwIDQwIDAgMCAxIDQwLTQwaDQ4YTQwLjAzIDQwLjAzIDAgMCAxIDQwIDQweiIgZmlsbD0iIzM0OGZkOSIvPjxwYXRoIGQ9Im0xNTIgMzA0djEzNmgtODh2LTk1LjA5YzI2LjE0LTE3LjE0IDUxLjE2LTQwLjQ4IDczLjk5LTcxLjNhMzkuODQ5IDM5Ljg0OSAwIDAgMSAxNC4wMSAzMC4zOXoiIGZpbGw9IiMzMDg2Y2QiLz48cGF0aCBkPSJtNjQgNDQwaDg4djQ4aC04OHoiIGZpbGw9IiM3YTQzMmEiLz48cGF0aCBkPSJtMTQ0IDQwOGgtODhhMzIgMzIgMCAwIDEgLTMyLTMydi00OGg0OHY0MGg0OGwyNC04eiIgZmlsbD0iI2ZlYzlhMyIvPjxwYXRoIGQ9Im00ODAgNDg4aC0xMjh2LTIwOGg5NmwzLjI1IDI2LjAyIDEyLjc1IDEwMS45OHoiIGZpbGw9IiM3ZWI0NTciLz48cGF0aCBkPSJtNDgwIDQ4OGgtMTI4di05OC4yMWMzNS45Ni0xNi4zOCA3MC4xOC00My4xNCA5OS4yNS04My43N2wxMi43NSAxMDEuOTh6IiBmaWxsPSIjNzlhZDU0Ii8+PHBhdGggZD0ibTM1MiAyODBhMCAwIDAgMCAxIDAgMHYxMDRhMCAwIDAgMCAxIDAgMGgtNDBhMCAwIDAgMCAxIDAgMHYtNjRhNDAgNDAgMCAwIDEgNDAtNDB6IiBmaWxsPSIjZmViNzg0Ii8+PHBhdGggZD0ibTQ0OCAyODB2ODhoLTY0djQwaDcyYTMyIDMyIDAgMCAwIDMyLTMydi01NmE0MCA0MCAwIDAgMCAtNDAtNDB6IiBmaWxsPSIjZmViNzg0Ii8+PHBhdGggZD0ibTE1MiAyMDh2MjRhNDggNDggMCAwIDEgLTQ4IDQ4Yy0uNzMgMC0xLjQ2LS4wMi0yLjE4LS4wNWE0OCA0OCAwIDAgMSAtNDUuODItNDcuOTV2LTI0YTQ4IDQ4IDAgMCAxIDQ4LTQ4cTIuMTE1IDAgNC4xNy4xOGE0OC4wMDcgNDguMDA3IDAgMCAxIDQzLjgzIDQ3LjgyeiIgZmlsbD0iI2ZlYzlhMyIvPjxwYXRoIGQ9Im0xNTIgMjA4djI0YTQ4IDQ4IDAgMCAxIC00OCA0OGMtLjczIDAtMS40Ni0uMDItMi4xOC0uMDVhNzEuNzEzIDcxLjcxMyAwIDAgMCAxOC4zMy00Ny45OXYtMzJhNzEuNjI5IDcxLjYyOSAwIDAgMCAtMTEuOTgtMzkuNzggNDguMDA3IDQ4LjAwNyAwIDAgMSA0My44MyA0Ny44MnoiIGZpbGw9IiNmZWMwOTMiLz48cGF0aCBkPSJtODAgMjE2aDE2djE2aC0xNnoiIGZpbGw9IiM3YTQzMmEiLz48cGF0aCBkPSJtMTEyIDIxNmgxNnYxNmgtMTZ6IiBmaWxsPSIjN2E0MzJhIi8+PHBhdGggZD0ibTU2IDIwOHYtMTZhMjQgMjQgMCAwIDEgMjQtMjR6IiBmaWxsPSIjODA0YTMyIi8+PHBhdGggZD0ibTE1MiAxODR2MjRsLTMyLTI0aC00MGEyNCAyNCAwIDAgMSAtMjQtMjR2LThoNjRhMzIgMzIgMCAwIDEgMzIgMzJ6IiBmaWxsPSIjOTI1NjNhIi8+PHBhdGggZD0ibTQ1NiAxODRoLTI0djMyaDI0djMyYTMyIDMyIDAgMCAwIDMyIDMydi02NGEzMiAzMiAwIDAgMCAtMzItMzJ6IiBmaWxsPSIjZjdhMTE2Ii8+PHBhdGggZD0ibTQ1NiAyMjR2MjRhNDcuOTk0IDQ3Ljk5NCAwIDAgMSAtNDIuOTMgNDcuNzMgNDcuMjc4IDQ3LjI3OCAwIDAgMSAtNS4wNy4yNyA0OCA0OCAwIDAgMSAtNDgtNDh2LTI0YTQ4IDQ4IDAgMCAxIDQ4LTQ4YzEuMTcgMCAyLjMzLjA0IDMuNDguMTNhNDggNDggMCAwIDEgNDQuNTIgNDcuODd6IiBmaWxsPSIjZmVjOWEzIi8+PHBhdGggZD0ibTQ1NiAyMjR2MjRhNDcuOTk0IDQ3Ljk5NCAwIDAgMSAtNDIuOTMgNDcuNzMgNzEuNjY0IDcxLjY2NCAwIDAgMCAxNC4wOC00Mi43N3YtMzJhNzEuNjQyIDcxLjY0MiAwIDAgMCAtMTUuNjctNDQuODMgNDggNDggMCAwIDEgNDQuNTIgNDcuODd6IiBmaWxsPSIjZmVjMDkzIi8+PHBhdGggZD0ibTM4NCAyMzJoMTZ2MTZoLTE2eiIgZmlsbD0iIzdhNDMyYSIvPjxwYXRoIGQ9Im00MTYgMjMyaDE2djE2aC0xNnoiIGZpbGw9IiM3YTQzMmEiLz48cGF0aCBkPSJtMzYwIDIzMnM0MCAwIDY0LTMyYzAgMCA4IDI0IDMyIDMydi0xNmE0OCA0OCAwIDAgMCAtNDgtNDggNDggNDggMCAwIDAgLTQ4IDQ4eiIgZmlsbD0iI2ZmYjUzMSIvPjxwYXRoIGQ9Im0zNjAgMzY4aDMydjg4aC0zMnoiIGZpbGw9IiNmZWM5YTMiLz48cGF0aCBkPSJtNDAgMjU2aDhhMTYgMTYgMCAwIDEgMTYgMTZ2MTZhMCAwIDAgMCAxIDAgMGgtNDBhMCAwIDAgMCAxIDAgMHYtMTZhMTYgMTYgMCAwIDEgMTYtMTZ6IiBmaWxsPSIjZmVjOWEzIi8+PHBhdGggZD0ibTI3MiA0ODhoLTE0NGwxMy4xNi02NS44MiAyLjg0LTE0LjE4di00MGEzMiAzMiAwIDAgMSAzMi0zMmg0OGEzMS45IDMxLjkgMCAwIDEgMjIuNjMgOS4zN2MuNTQuNTQgMS4wNSAxLjA5IDEuNTUgMS42N2EzMS44NjcgMzEuODY3IDAgMCAxIDcuODIgMjAuOTZ2NDB6IiBmaWxsPSIjZjU5ODk4Ii8+PHBhdGggZD0ibTI3MiA0ODhoLTE0NGwxMy4xNi02NS44MmMzOC0xMy45MyA3NC43Ny0zNy44NSAxMDcuMDItNzUuMTRhMzEuODY3IDMxLjg2NyAwIDAgMSA3LjgyIDIwLjk2djQweiIgZmlsbD0iI2VkOTE5MSIvPjxwYXRoIGQ9Im0xNTIgNDU2aDMybC04LTgwaC0zMnoiIGZpbGw9IiNmZWM5YTMiLz48cGF0aCBkPSJtMjQ4IDQ1NmgtMzJsOC04MGgzMnoiIGZpbGw9IiNmZWI3ODQiLz48cGF0aCBkPSJtMTIwIDMyOHYtNDhhMzIgMzIgMCAwIDEgMzItMzJoMjR2MzJoLTI0djE2YTMyIDMyIDAgMCAxIC0zMiAzMnoiIGZpbGw9IiNmNTc3MDciLz48cGF0aCBkPSJtMjQ4IDI3MnYxNmE0OCA0OCAwIDAgMSAtOTYgMHYtMTZhNDggNDggMCAwIDEgNDgtNDggNDggNDggMCAwIDEgNDggNDh6IiBmaWxsPSIjZmVjOWEzIi8+PHBhdGggZD0ibTI0OCAyNzJ2MTZhNDguMDI2IDQ4LjAyNiAwIDAgMSAtMzIgNDUuMjcgNzEuNjgxIDcxLjY4MSAwIDAgMCA3LjE1LTMxLjMxdi0zMmE3MS43IDcxLjcgMCAwIDAgLTE2LjE2LTQ1LjQ1IDQ4LjAwOSA0OC4wMDkgMCAwIDEgNDEuMDEgNDcuNDl6IiBmaWxsPSIjZmVjMDkzIi8+PHBhdGggZD0ibTE3NiAyODBoMTZ2MTZoLTE2eiIgZmlsbD0iIzdhNDMyYSIvPjxwYXRoIGQ9Im0yMDggMjgwaDE2djE2aC0xNnoiIGZpbGw9IiM3YTQzMmEiLz48cGF0aCBkPSJtMjQ4IDI3MmgtNy4wMTVhNDIuMjQ2IDQyLjI0NiAwIDAgMSAtNDAuOTg1LTMyIDQyLjI0NiA0Mi4yNDYgMCAwIDEgLTQwLjk4NSAzMmgtNy4wMTV2LThhNDggNDggMCAwIDEgNDgtNDggNDggNDggMCAwIDEgNDggNDh6IiBmaWxsPSIjZjk4NTAwIi8+PHBhdGggZD0ibTM2OCAyNDh2MTZhNDggNDggMCAwIDEgLTQ0LjYxIDQ3Ljg4cS0xLjY4LjEyLTMuMzkuMTJhNDggNDggMCAwIDEgLTQ4LTQ4di0xNmE0OCA0OCAwIDAgMSA0OC00OCA0Ni4xNjIgNDYuMTYyIDAgMCAxIDQuODcuMjUgNDggNDggMCAwIDEgNDMuMTMgNDcuNzV6IiBmaWxsPSIjZmVjOWEzIi8+PHBhdGggZD0ibTM2OCAyNDh2MTZhNDggNDggMCAwIDEgLTQ0LjYxIDQ3Ljg4IDcxLjYgNzEuNiAwIDAgMCAxMi43Ni00MC45MnYtMzJhNzEuNjc2IDcxLjY3NiAwIDAgMCAtMTEuMjgtMzguNzEgNDggNDggMCAwIDEgNDMuMTMgNDcuNzV6IiBmaWxsPSIjZmVjMDkzIi8+PHBhdGggZD0ibTM0NCAyMDhzLTggMzIgMjQgNDBhNDggNDggMCAwIDAgLTQ4LTQ4IDQ4IDQ4IDAgMCAwIC00Ny4zMjIgMzkuOTkxYzYuMzg3LS4xMjQgNTYuMzU0LTIuMDU2IDcxLjMyMi0zMS45OTF6IiBmaWxsPSIjOTI1NjNhIi8+PHBhdGggZD0ibTI5NiAyNTZoMTZ2MTZoLTE2eiIgZmlsbD0iIzdhNDMyYSIvPjxwYXRoIGQ9Im0zMjggMjU2aDE2djE2aC0xNnoiIGZpbGw9IiM3YTQzMmEiLz48cGF0aCBkPSJtMzkyIDM0NHYyNGgtMzJ2NDhoLTgwdi00OGgtMzJ2LTI0YTMyIDMyIDAgMCAxIDMyLTMyaDgwYTMxLjk1IDMxLjk1IDAgMCAxIDMyIDMyeiIgZmlsbD0iIzM0OGZkOSIvPjxwYXRoIGQ9Im0zOTIgMzQ0djI0aC0zMnY0OGgtODB2LTMyLjg3YzMyLjkzLTE0LjQ1IDY0LjQ4LTM2LjYgOTIuNDQtNjguNjNhMzIuMDMzIDMyLjAzMyAwIDAgMSAxOS41NiAyOS41eiIgZmlsbD0iIzMwODZjZCIvPjxwYXRoIGQ9Im0yODAgNDE2aDgwdjcyaC04MHoiIGZpbGw9IiM3YTQzMmEiLz48cGF0aCBkPSJtMzEyIDQ0MGgxNnY0OGgtMTZ6IiBmaWxsPSIjNWMyZTFhIi8+PHBhdGggZD0ibTI0OCAzNjhoMzJ2ODhoLTMyeiIgZmlsbD0iI2ZlYzlhMyIvPjxyZWN0IGZpbGw9IiMyYTcxYWQiIGhlaWdodD0iMzIiIHJ4PSI4IiB3aWR0aD0iMTYiIHg9IjI3MiIgeT0iMzQ0Ii8+PHJlY3QgZmlsbD0iIzJhNzFhZCIgaGVpZ2h0PSIzMiIgcng9IjgiIHdpZHRoPSIxNiIgeD0iMzUyIiB5PSIzNDQiLz48L2c+PC9zdmc+" />
            <p class="mb-0 font-weight-bold mt-1" style="color:IndianRed;">연령별</p>
          </div>
          <div class="col" @click="giveFlag(4)">
            <img style="width:45px;" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pg0KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjAuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPg0KPHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJDYXBhXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4Ig0KCSB2aWV3Qm94PSIwIDAgNTEyLjAwMyA1MTIuMDAzIiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA1MTIuMDAzIDUxMi4wMDM7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4NCjxwYXRoIHN0eWxlPSJmaWxsOiM4MEM3RUE7IiBkPSJNNTEyLjAwMiwyNTZjMC03LjQxNS02LjAxMS0xMy40MjctMTMuNDI3LTEzLjQyN2gtMjEuMTI3bDIwLjExMy0yMC4xMTMNCgljNS4yNDQtNS4yNDQsNS4yNDQtMTMuNzQ2LDAtMTguOTg5cy0xMy43NDUtNS4yNDQtMTguOTg5LDBsLTM5LjEwMywzOS4xMDNoLTE5Ljg3NWwyMC4xMTMtMjAuMTEzDQoJYzUuMjQ0LTUuMjQ0LDUuMjQ0LTEzLjc0NiwwLTE4Ljk4OWMtNS4yNDUtNS4yNDQtMTMuNzQ2LTUuMjQ0LTE4Ljk4OSwwbC0zOS4xMDMsMzkuMTAzaC05My4xOTdsNjUuOTAxLTY1LjkwMWg1NS4yOTkNCgljNy40MTYsMCwxMy40MjctNi4wMTEsMTMuNDI3LTEzLjQyN3MtNi4wMTEtMTMuNDI3LTEzLjQyNy0xMy40MjdoLTI4LjQ0NGwxNC4wNTQtMTQuMDU0aDU1LjI5OWM3LjQxNiwwLDEzLjQyNy02LjAxMSwxMy40MjctMTMuNDI3DQoJYzAtNy40MTYtNi4wMTEtMTMuNDI3LTEzLjQyNy0xMy40MjdoLTI4LjQ0NGwxNC45NC0xNC45NGM1LjI0NC01LjI0NCw1LjI0NC0xMy43NDYsMC0xOC45ODljLTUuMjQ0LTUuMjQ0LTEzLjc0Ni01LjI0NC0xOC45ODksMA0KCWwtMTQuOTQsMTQuOTRWNjEuNDc1YzAtNy40MTYtNi4wMTEtMTMuNDI3LTEzLjQyNy0xMy40MjdzLTEzLjQyNyw2LjAxMS0xMy40MjcsMTMuNDI3djU1LjI5OWwtMTQuMDU0LDE0LjA1NHYtMjguNDQzDQoJYzAtNy40MTYtNi4wMTEtMTMuNDI3LTEzLjQyNy0xMy40MjdjLTcuNDE2LDAtMTMuNDI3LDYuMDExLTEzLjQyNywxMy40Mjd2NTUuMjk5bC02NS45MDEsNjUuOTAxdi05My4xOTdsMzkuMTAzLTM5LjEwMw0KCWM1LjI0NC01LjI0NCw1LjI0NC0xMy43NDYsMC0xOC45ODljLTUuMjQ1LTUuMjQ0LTEzLjc0Ni01LjI0NC0xOC45ODksMGwtMjAuMTE0LDIwLjExM1Y3Mi41MzNsMzkuMTAzLTM5LjEwMw0KCWM1LjI0NC01LjI0NCw1LjI0NC0xMy43NDYsMC0xOC45ODljLTUuMjQ1LTUuMjQ0LTEzLjc0Ni01LjI0NC0xOC45ODksMGwtMjAuMTE0LDIwLjExM1YxMy40MjdDMjY5LjQyOSw2LjAxMSwyNjMuNDE4LDAsMjU2LjAwMiwwDQoJYy03LjQxNSwwLTEzLjQyNyw2LjAxMS0xMy40MjcsMTMuNDI3djIxLjEyN2wtMjAuMTEzLTIwLjExM2MtNS4yNDQtNS4yNDQtMTMuNzQ1LTUuMjQ0LTE4Ljk4OSwwDQoJYy01LjI0NCw1LjI0NC01LjI0NCwxMy43NDYsMCwxOC45ODlsMzkuMTAzLDM5LjEwM3YxOS44NzZsLTIwLjExMy0yMC4xMTNjLTUuMjQ0LTUuMjQ0LTEzLjc0NS01LjI0NC0xOC45ODksMA0KCWMtNS4yNDQsNS4yNDQtNS4yNDQsMTMuNzQ2LDAsMTguOTg5bDM5LjEwMywzOS4xMDN2OTMuMTk3bC02NS45MDEtNjUuOTAxdi01NS4zYzAtNy40MTYtNi4wMTEtMTMuNDI3LTEzLjQyNy0xMy40MjcNCglzLTEzLjQyNyw2LjAxMS0xMy40MjcsMTMuNDI3djI4LjQ0NGwtMTQuMDU0LTE0LjA1NHYtNTUuM2MwLTcuNDE2LTYuMDExLTEzLjQyNy0xMy40MjctMTMuNDI3Yy03LjQxNiwwLTEzLjQyNyw2LjAxMS0xMy40MjcsMTMuNDI3DQoJdjI4LjQ0NEw5My45NzIsNzQuOTgxYy01LjI0NC01LjI0NC0xMy43NDYtNS4yNDQtMTguOTg5LDBjLTUuMjQ0LDUuMjQ0LTUuMjQ0LDEzLjc0NiwwLDE4Ljk4OWwxNC45NCwxNC45NEg2MS40NzcNCgljLTcuNDE2LDAtMTMuNDI3LDYuMDExLTEzLjQyNywxMy40MjdzNi4wMTEsMTMuNDI3LDEzLjQyNywxMy40MjdoNTUuMjk5bDE0LjA1NCwxNC4wNTRoLTI4LjQ0Mw0KCWMtNy40MTYsMC0xMy40MjcsNi4wMTEtMTMuNDI3LDEzLjQyN3M2LjAxMSwxMy40MjcsMTMuNDI3LDEzLjQyN2g1NS4yOTlsNjUuOTAxLDY1LjkwMWgtOTMuMTk3TDkxLjI4NiwyMDMuNDcNCgljLTUuMjQ0LTUuMjQ0LTEzLjc0NS01LjI0NC0xOC45ODksMGMtNS4yNDQsNS4yNDQtNS4yNDQsMTMuNzQ2LDAsMTguOTg5bDIwLjExMywyMC4xMTNINzIuNTM1TDMzLjQzMiwyMDMuNDcNCgljLTUuMjQ0LTUuMjQ0LTEzLjc0NS01LjI0NC0xOC45ODksMGMtNS4yNDQsNS4yNDQtNS4yNDQsMTMuNzQ2LDAsMTguOTg5bDIwLjExMywyMC4xMTNIMTMuNDI5Yy03LjQxNiwwLTEzLjQyNyw2LjAxMi0xMy40MjcsMTMuNDI3DQoJYzAsNy40MTYsNi4wMTEsMTMuNDI3LDEzLjQyNywxMy40MjdoMjEuMTI4bC0yMC4xMTMsMjAuMTE0Yy01LjI0NCw1LjI0NC01LjI0NCwxMy43NDYsMCwxOC45ODkNCgljMi42MjIsMi42MjIsNi4wNTgsMy45MzMsOS40OTQsMy45MzNzNi44NzMtMS4zMTEsOS40OTQtMy45MzNsMzkuMTAzLTM5LjEwM2gxOS44NzZsLTIwLjExMywyMC4xMTQNCgljLTUuMjQ0LDUuMjQ0LTUuMjQ0LDEzLjc0NiwwLDE4Ljk4OWMyLjYyMiwyLjYyMiw2LjA1OCwzLjkzMyw5LjQ5NCwzLjkzM3M2Ljg3My0xLjMxMSw5LjQ5NC0zLjkzM2wzOS4xMDMtMzkuMTAzaDkzLjE5Nw0KCWwtNjUuOTAxLDY1LjkwMWgtNTUuMjk5Yy03LjQxNiwwLTEzLjQyNyw2LjAxMS0xMy40MjcsMTMuNDI3YzAsNy40MTYsNi4wMTEsMTMuNDI3LDEzLjQyNywxMy40MjdoMjguNDQ0bC0xNC4wNTQsMTQuMDU0aC01NS4zDQoJYy03LjQxNiwwLTEzLjQyNyw2LjAxMS0xMy40MjcsMTMuNDI3czYuMDExLDEzLjQyNywxMy40MjcsMTMuNDI3aDI4LjQ0NGwtMTQuOTQsMTQuOTRjLTUuMjQ0LDUuMjQ0LTUuMjQ0LDEzLjc0NSwwLDE4Ljk4OQ0KCWMyLjYyMiwyLjYyMiw2LjA1OCwzLjkzMyw5LjQ5NCwzLjkzM3M2Ljg3My0xLjMxMSw5LjQ5NC0zLjkzM2wxNC45NC0xNC45NHYyOC40NDRjMCw3LjQxNiw2LjAxMSwxMy40MjcsMTMuNDI3LDEzLjQyNw0KCWM3LjQxNiwwLDEzLjQyNy02LjAxMSwxMy40MjctMTMuNDI3di01NS4yOTlsMTQuMDU0LTE0LjA1NHYyOC40NDRjMCw3LjQxNiw2LjAxMSwxMy40MjcsMTMuNDI3LDEzLjQyN3MxMy40MjctNi4wMTEsMTMuNDI3LTEzLjQyNw0KCXYtNTUuMjk5bDY1LjkwMS02NS45MDF2OTMuMTk3bC0zOS4xMDMsMzkuMTAzYy01LjI0NCw1LjI0NC01LjI0NCwxMy43NDYsMCwxOC45ODljNS4yNDQsNS4yNDQsMTMuNzQ2LDUuMjQ0LDE4Ljk4OSwwbDIwLjExMy0yMC4xMTMNCgl2MTkuODc1bC0zOS4xMDMsMzkuMTAzYy01LjI0NCw1LjI0NC01LjI0NCwxMy43NDYsMCwxOC45ODljMi42MjIsMi42MjIsNi4wNTgsMy45MzMsOS40OTQsMy45MzNjMy40MzcsMCw2Ljg3My0xLjMxMSw5LjQ5NC0zLjkzMw0KCWwyMC4xMTMtMjAuMTEzdjIxLjEyN2MwLDcuNDE2LDYuMDEyLDEzLjQyNywxMy40MjcsMTMuNDI3YzcuNDE2LDAsMTMuNDI3LTYuMDExLDEzLjQyNy0xMy40Mjd2LTIxLjEyN2wyMC4xMTQsMjAuMTE0DQoJYzUuMjQ0LDUuMjQ0LDEzLjc0Niw1LjI0NCwxOC45ODksMHM1LjI0NC0xMy43NDUsMC0xOC45ODlsLTM5LjEwMy0zOS4xMDN2LTE5Ljg3NmwyMC4xMTQsMjAuMTE0DQoJYzIuNjIyLDIuNjIyLDYuMDU5LDMuOTMzLDkuNDk0LDMuOTMzczYuODczLTEuMzExLDkuNDk0LTMuOTMzYzUuMjQ0LTUuMjQ0LDUuMjQ0LTEzLjc0NSwwLTE4Ljk4OWwtMzkuMTAzLTM5LjEwM1YyODguNDINCglsNjUuOTAxLDY1LjkwMXY1NS4yOTljMCw3LjQxNiw2LjAxMSwxMy40MjcsMTMuNDI3LDEzLjQyN2M3LjQxNiwwLDEzLjQyNy02LjAxMSwxMy40MjctMTMuNDI3di0yOC40NDRsMTQuMDU0LDE0LjA1NHY1NS4yOTkNCgljMCw3LjQxNiw2LjAxMSwxMy40MjcsMTMuNDI3LDEzLjQyN3MxMy40MjctNi4wMTEsMTMuNDI3LTEzLjQyN3YtMjguNDQ0bDE0Ljk0LDE0Ljk0YzIuNjIyLDIuNjIyLDYuMDU5LDMuOTMzLDkuNDk0LDMuOTMzDQoJYzMuNDM3LDAsNi44NzMtMS4zMTEsOS40OTQtMy45MzNjNS4yNDQtNS4yNDQsNS4yNDQtMTMuNzQ1LDAtMTguOTg5bC0xNC45NC0xNC45NGgyOC40NDRjNy40MTYsMCwxMy40MjctNi4wMTEsMTMuNDI3LTEzLjQyNw0KCWMwLTcuNDE2LTYuMDExLTEzLjQyNy0xMy40MjctMTMuNDI3aC01NS4yOTlsLTE0LjA1NC0xNC4wNTRoMjguNDQ0YzcuNDE2LDAsMTMuNDI3LTYuMDExLDEzLjQyNy0xMy40MjcNCgljMC03LjQxNi02LjAxMS0xMy40MjctMTMuNDI3LTEzLjQyN2gtNTUuMjk5bC02NS45MDEtNjUuOTAxaDkzLjE5N2wzOS4xMDMsMzkuMTAzYzIuNjIyLDIuNjIyLDYuMDU5LDMuOTMzLDkuNDk0LDMuOTMzDQoJczYuODczLTEuMzExLDkuNDk0LTMuOTMzYzUuMjQ0LTUuMjQ0LDUuMjQ0LTEzLjc0NSwwLTE4Ljk4OWwtMjAuMTE0LTIwLjExNGgxOS44NzZsMzkuMTAzLDM5LjEwMw0KCWMyLjYyMiwyLjYyMiw2LjA1OSwzLjkzMyw5LjQ5NCwzLjkzM2MzLjQzNiwwLDYuODczLTEuMzExLDkuNDk0LTMuOTMzYzUuMjQ0LTUuMjQ0LDUuMjQ0LTEzLjc0NSwwLTE4Ljk4OWwtMjAuMTE0LTIwLjExNGgyMS4xMjcNCglDNTA1Ljk5LDI2OS40MjcsNTEyLjAwMiwyNjMuNDE2LDUxMi4wMDIsMjU2eiIvPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPC9zdmc+DQo=" />
            <p class="mb-0 font-weight-bold mt-1" style="color:SteelBlue ;">계절별</p>
          </div>
        </div>    

        <div class="m-3 px-3">
            <div v-if="flag==0">
                <h5 class="my-auto font-weight-bold">남자 대학생 향수 추천</h5>
                <div class="container mb-5">
                    <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4" style="border:none; display:inline-block;" v-for="perfume in newStudentMen" :key="perfume.id">
                        <div @click="goDetail(perfume.id)" class="property-card" style="cursor:pointer;">
                            <div class="property-image" :style="{ backgroundImage: 'url(' + perfume.image + ')' }">
                                <div class="property-image-title">
                                    <!-- Optional <h5>Card Title</h5> If you want it, turn on the CSS also. -->
                                </div>
                            </div>
                            <div class="property-description">
                                <small class="mr-2" style="color:whitesmoke; font-weight:bold">{{perfume.brand}}</small>
                                <i v-if="perfume.gender==0" class="fas fa-venus" style="color:red"></i> 
                                <i v-if="perfume.gender==1" class="fas fa-mars" style="color:blue"></i>
                                <i v-if="perfume.gender==2" class="fas fa-venus-mars" style=""></i>
                                <h5 class="mt-2" style="font-size:1.2rem">{{perfume.name}}</h5>
                                <div class="d-flex justify-content-center my-2">
                                    <b-badge v-if="perfume.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                                    <div v-for="line in perfume.lineList" :key="line.id">
                                        <b-badge v-if="line == 'Floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <h5 class="font-weight-bold">여자 대학생 향수 추천</h5>
                <div class="container mb-5">
                    <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4" style="border:none; display:inline-block;" v-for="perfume in newStudentWomen" :key="perfume.id">
                        <div @click="goDetail(perfume.id)" class="property-card" style="cursor:pointer;">
                            <div class="property-image" :style="{ backgroundImage: 'url(' + perfume.image + ')' }">
                                <div class="property-image-title">
                                    <!-- Optional <h5>Card Title</h5> If you want it, turn on the CSS also. -->
                                </div>
                            </div>
                            <div class="property-description">
                                <small class="mr-2" style="color:whitesmoke; font-weight:bold">{{perfume.brand}}</small>
                                <i v-if="perfume.gender==0" class="fas fa-venus" style="color:red"></i> 
                                <i v-if="perfume.gender==1" class="fas fa-mars" style="color:blue"></i>
                                <i v-if="perfume.gender==2" class="fas fa-venus-mars" style=""></i>
                                <h5 class="mt-2" style="font-size:1.2rem">{{perfume.name}}</h5>
                                <div class="d-flex justify-content-center my-2">
                                    <b-badge v-if="perfume.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                                    <div v-for="line in perfume.lineList" :key="line.id">
                                        <b-badge v-if="line == 'Floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>    

            <div v-if="flag==2">
                <h5 class="font-weight-bold">남자 사회초년생 향수 추천</h5>
                <div class="container mb-5">
                    <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4" style="border:none; display:inline-block;" v-for="perfume in socialMen" :key="perfume.id">
                        <div @click="goDetail(perfume.id)" class="property-card" style="cursor:pointer;">
                            <div class="property-image" :style="{ backgroundImage: 'url(' + perfume.image + ')' }">
                                <div class="property-image-title">
                                    <!-- Optional <h5>Card Title</h5> If you want it, turn on the CSS also. -->
                                </div>
                            </div>
                            <div class="property-description">
                                <small class="mr-2" style="color:whitesmoke; font-weight:bold">{{perfume.brand}}</small>
                                <i v-if="perfume.gender==0" class="fas fa-venus" style="color:red"></i> 
                                <i v-if="perfume.gender==1" class="fas fa-mars" style="color:blue"></i>
                                <i v-if="perfume.gender==2" class="fas fa-venus-mars" style=""></i>
                                <h5 class="mt-2" style="font-size:1.2rem">{{perfume.name}}</h5>
                                <div class="d-flex justify-content-center my-2">
                                    <b-badge v-if="perfume.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                                    <div v-for="line in perfume.lineList" :key="line.id">
                                        <b-badge v-if="line == 'Floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <h5 class="font-weight-bold">여자 사회초년생 향수 추천</h5>
                <div class="container mb-5">
                    <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4" style="border:none; display:inline-block;" v-for="perfume in socialWomen" :key="perfume.id">
                        <div @click="goDetail(perfume.id)" class="property-card" style="cursor:pointer;">
                            <div class="property-image" :style="{ backgroundImage: 'url(' + perfume.image + ')' }">
                                <div class="property-image-title">
                                    <!-- Optional <h5>Card Title</h5> If you want it, turn on the CSS also. -->
                                </div>
                            </div>
                            <div class="property-description">
                                <small class="mr-2" style="color:whitesmoke; font-weight:bold">{{perfume.brand}}</small>
                                <i v-if="perfume.gender==0" class="fas fa-venus" style="color:red"></i> 
                                <i v-if="perfume.gender==1" class="fas fa-mars" style="color:blue"></i>
                                <i v-if="perfume.gender==2" class="fas fa-venus-mars" style=""></i>
                                <h5 class="mt-2" style="font-size:1.2rem">{{perfume.name}}</h5>
                                <div class="d-flex justify-content-center my-2">
                                    <b-badge v-if="perfume.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                                    <div v-for="line in perfume.lineList" :key="line.id">
                                        <b-badge v-if="line == 'Floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div v-if="flag==3">
                <h5 class="font-weight-bold">30대 남성 향수 추천</h5>
                <div class="container">
                    <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4" style="border:none; display:inline-block;" v-for="perfume in thirtyMen" :key="perfume.id">
                        <div @click="goDetail(perfume.id)" class="property-card" style="cursor:pointer;">
                            <div class="property-image" :style="{ backgroundImage: 'url(' + perfume.image + ')' }">
                                <div class="property-image-title">
                                    <!-- Optional <h5>Card Title</h5> If you want it, turn on the CSS also. -->
                                </div>
                            </div>
                            <div class="property-description">
                                <small class="mr-2" style="color:whitesmoke; font-weight:bold">{{perfume.brand}}</small>
                                <i v-if="perfume.gender==0" class="fas fa-venus" style="color:red"></i> 
                                <i v-if="perfume.gender==1" class="fas fa-mars" style="color:blue"></i>
                                <i v-if="perfume.gender==2" class="fas fa-venus-mars" style=""></i>
                                <h5 class="mt-2" style="font-size:1.2rem">{{perfume.name}}</h5>
                                <div class="d-flex justify-content-center my-2">
                                    <b-badge v-if="perfume.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                                    <div v-for="line in perfume.lineList" :key="line.id">
                                        <b-badge v-if="line == 'Floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>


                <h5 class="font-weight-bold">30대 여성 향수 추천</h5>
                <div class="container">
                    <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4" style="border:none; display:inline-block;" v-for="perfume in thirtyWomen" :key="perfume.id">
                        <div @click="goDetail(perfume.id)" class="property-card" style="cursor:pointer;">
                            <div class="property-image" :style="{ backgroundImage: 'url(' + perfume.image + ')' }">
                                <div class="property-image-title">
                                    <!-- Optional <h5>Card Title</h5> If you want it, turn on the CSS also. -->
                                </div>
                            </div>
                            <div class="property-description">
                                <small class="mr-2" style="color:whitesmoke; font-weight:bold">{{perfume.brand}}</small>
                                <i v-if="perfume.gender==0" class="fas fa-venus" style="color:red"></i> 
                                <i v-if="perfume.gender==1" class="fas fa-mars" style="color:blue"></i>
                                <i v-if="perfume.gender==2" class="fas fa-venus-mars" style=""></i>
                                <h5 class="mt-2" style="font-size:1.2rem">{{perfume.name}}</h5>
                                <div class="d-flex justify-content-center my-2">
                                    <b-badge v-if="perfume.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                                    <div v-for="line in perfume.lineList" :key="line.id">
                                        <b-badge v-if="line == 'Floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <h5 class="font-weight-bold">40대 남성 향수 추천</h5>
                <div class="container">
                    <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4" style="border:none; display:inline-block;" v-for="perfume in fortyMen" :key="perfume.id">
                        <div @click="goDetail(perfume.id)" class="property-card" style="cursor:pointer;">
                            <div class="property-image" :style="{ backgroundImage: 'url(' + perfume.image + ')' }">
                                <div class="property-image-title">
                                    <!-- Optional <h5>Card Title</h5> If you want it, turn on the CSS also. -->
                                </div>
                            </div>
                            <div class="property-description">
                                <small class="mr-2" style="color:whitesmoke; font-weight:bold">{{perfume.brand}}</small>
                                <i v-if="perfume.gender==0" class="fas fa-venus" style="color:red"></i> 
                                <i v-if="perfume.gender==1" class="fas fa-mars" style="color:blue"></i>
                                <i v-if="perfume.gender==2" class="fas fa-venus-mars" style=""></i>
                                <h5 class="mt-2" style="font-size:1.2rem">{{perfume.name}}</h5>
                                <div class="d-flex justify-content-center my-2">
                                    <b-badge v-if="perfume.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                                    <div v-for="line in perfume.lineList" :key="line.id">
                                        <b-badge v-if="line == 'Floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                
                <h5 class="font-weight-bold">40대 여성 향수 추천</h5>
                <div class="container">
                    <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4" style="border:none; display:inline-block;" v-for="perfume in fortyWomen" :key="perfume.id">
                        <div @click="goDetail(perfume.id)" class="property-card" style="cursor:pointer;">
                            <div class="property-image" :style="{ backgroundImage: 'url(' + perfume.image + ')' }">
                                <div class="property-image-title">
                                    <!-- Optional <h5>Card Title</h5> If you want it, turn on the CSS also. -->
                                </div>
                            </div>
                            <div class="property-description">
                                <small class="mr-2" style="color:whitesmoke; font-weight:bold">{{perfume.brand}}</small>
                                <i v-if="perfume.gender==0" class="fas fa-venus" style="color:red"></i> 
                                <i v-if="perfume.gender==1" class="fas fa-mars" style="color:blue"></i>
                                <i v-if="perfume.gender==2" class="fas fa-venus-mars" style=""></i>
                                <h5 class="mt-2" style="font-size:1.2rem">{{perfume.name}}</h5>
                                <div class="d-flex justify-content-center my-2">
                                    <b-badge v-if="perfume.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                                    <div v-for="line in perfume.lineList" :key="line.id">
                                        <b-badge v-if="line == 'Floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                
                <h5 class="font-weight-bold">50대 남성 향수 추천</h5>
                <div class="container">
                    <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4" style="border:none; display:inline-block;" v-for="perfume in fiftyMen" :key="perfume.id">
                        <div @click="goDetail(perfume.id)" class="property-card" style="cursor:pointer;">
                            <div class="property-image" :style="{ backgroundImage: 'url(' + perfume.image + ')' }">
                                <div class="property-image-title">
                                    <!-- Optional <h5>Card Title</h5> If you want it, turn on the CSS also. -->
                                </div>
                            </div>
                            <div class="property-description">
                                <small class="mr-2" style="color:whitesmoke; font-weight:bold">{{perfume.brand}}</small>
                                <i v-if="perfume.gender==0" class="fas fa-venus" style="color:red"></i> 
                                <i v-if="perfume.gender==1" class="fas fa-mars" style="color:blue"></i>
                                <i v-if="perfume.gender==2" class="fas fa-venus-mars" style=""></i>
                                <h5 class="mt-2" style="font-size:1.2rem">{{perfume.name}}</h5>
                                <div class="d-flex justify-content-center my-2">
                                    <b-badge v-if="perfume.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                                    <div v-for="line in perfume.lineList" :key="line.id">
                                        <b-badge v-if="line == 'Floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                    
                <h5 class="font-weight-bold">50대 여성 향수 추천</h5>
                <div class="container">
                    <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4" style="border:none; display:inline-block;" v-for="perfume in fiftyWomen" :key="perfume.id">
                        <div @click="goDetail(perfume.id)" class="property-card" style="cursor:pointer;">
                            <div class="property-image" :style="{ backgroundImage: 'url(' + perfume.image + ')' }">
                                <div class="property-image-title">
                                    <!-- Optional <h5>Card Title</h5> If you want it, turn on the CSS also. -->
                                </div>
                            </div>
                            <div class="property-description">
                                <small class="mr-2" style="color:whitesmoke; font-weight:bold">{{perfume.brand}}</small>
                                <i v-if="perfume.gender==0" class="fas fa-venus" style="color:red"></i> 
                                <i v-if="perfume.gender==1" class="fas fa-mars" style="color:blue"></i>
                                <i v-if="perfume.gender==2" class="fas fa-venus-mars" style=""></i>
                                <h5 class="mt-2" style="font-size:1.2rem">{{perfume.name}}</h5>
                                <div class="d-flex justify-content-center my-2">
                                    <b-badge v-if="perfume.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                                    <div v-for="line in perfume.lineList" :key="line.id">
                                        <b-badge v-if="line == 'Floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div v-if="flag==4">
                <h5 class="font-weight-bold">봄 향수 추천</h5>
                <div class="container mb-5">
                    <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4" style="border:none; display:inline-block;" v-for="perfume in springPerfume" :key="perfume.id">
                        <div @click="goDetail(perfume.id)" class="property-card" style="cursor:pointer;">
                            <div class="property-image" :style="{ backgroundImage: 'url(' + perfume.image + ')' }">
                                <div class="property-image-title">
                                    <!-- Optional <h5>Card Title</h5> If you want it, turn on the CSS also. -->
                                </div>
                            </div>
                            <div class="property-description">
                                <small class="mr-2" style="color:whitesmoke; font-weight:bold">{{perfume.brand}}</small>
                                <i v-if="perfume.gender==0" class="fas fa-venus" style="color:red"></i> 
                                <i v-if="perfume.gender==1" class="fas fa-mars" style="color:blue"></i>
                                <i v-if="perfume.gender==2" class="fas fa-venus-mars" style=""></i>
                                <h5 class="mt-2" style="font-size:1.2rem">{{perfume.name}}</h5>
                                <div class="d-flex justify-content-center my-2">
                                    <b-badge v-if="perfume.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                                    <div v-for="line in perfume.lineList" :key="line.id">
                                        <b-badge v-if="line == 'Floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>


                <h5 class="font-weight-bold">여름 향수 추천</h5>
                <div class="container mb-5">
                    <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4" style="border:none; display:inline-block;" v-for="perfume in summerPerfume" :key="perfume.id">
                        <div @click="goDetail(perfume.id)" class="property-card" style="cursor:pointer;">
                            <div class="property-image" :style="{ backgroundImage: 'url(' + perfume.image + ')' }">
                                <div class="property-image-title">
                                    <!-- Optional <h5>Card Title</h5> If you want it, turn on the CSS also. -->
                                </div>
                            </div>
                            <div class="property-description">
                                <small class="mr-2" style="color:whitesmoke; font-weight:bold">{{perfume.brand}}</small>
                                <i v-if="perfume.gender==0" class="fas fa-venus" style="color:red"></i> 
                                <i v-if="perfume.gender==1" class="fas fa-mars" style="color:blue"></i>
                                <i v-if="perfume.gender==2" class="fas fa-venus-mars" style=""></i>
                                <h5 class="mt-2" style="font-size:1.2rem">{{perfume.name}}</h5>
                                <div class="d-flex justify-content-center my-2">
                                    <b-badge v-if="perfume.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                                    <div v-for="line in perfume.lineList" :key="line.id">
                                        <b-badge v-if="line == 'Floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>


                <h5 class="font-weight-bold">가을 향수 추천</h5>
                <div class="container mb-5">
                    <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4" style="border:none; display:inline-block;" v-for="perfume in autumnPerfume" :key="perfume.id">
                        <div @click="goDetail(perfume.id)" class="property-card" style="cursor:pointer;">
                            <div class="property-image" :style="{ backgroundImage: 'url(' + perfume.image + ')' }">
                                <div class="property-image-title">
                                    <!-- Optional <h5>Card Title</h5> If you want it, turn on the CSS also. -->
                                </div>
                            </div>
                            <div class="property-description">
                                <small class="mr-2" style="color:whitesmoke; font-weight:bold">{{perfume.brand}}</small>
                                <i v-if="perfume.gender==0" class="fas fa-venus" style="color:red"></i> 
                                <i v-if="perfume.gender==1" class="fas fa-mars" style="color:blue"></i>
                                <i v-if="perfume.gender==2" class="fas fa-venus-mars" style=""></i>
                                <h5 class="mt-2" style="font-size:1.2rem">{{perfume.name}}</h5>
                                <div class="d-flex justify-content-center my-2">
                                    <b-badge v-if="perfume.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                                    <div v-for="line in perfume.lineList" :key="line.id">
                                        <b-badge v-if="line == 'Floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>


                <h5 class="font-weight-bold">겨울 향수 추천</h5>
                <div class="container mb-5">
                    <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4" style="border:none; display:inline-block;" v-for="perfume in winterPerfume" :key="perfume.id">
                        <div @click="goDetail(perfume.id)" class="property-card" style="cursor:pointer;">
                            <div class="property-image" :style="{ backgroundImage: 'url(' + perfume.image + ')' }">
                                <div class="property-image-title">
                                    <!-- Optional <h5>Card Title</h5> If you want it, turn on the CSS also. -->
                                </div>
                            </div>
                            <div class="property-description">
                                <small class="mr-2" style="color:whitesmoke; font-weight:bold">{{perfume.brand}}</small>
                                <i v-if="perfume.gender==0" class="fas fa-venus" style="color:red"></i> 
                                <i v-if="perfume.gender==1" class="fas fa-mars" style="color:blue"></i>
                                <i v-if="perfume.gender==2" class="fas fa-venus-mars" style=""></i>
                                <h5 class="mt-2" style="font-size:1.2rem">{{perfume.name}}</h5>
                                <div class="d-flex justify-content-center my-2">
                                    <b-badge v-if="perfume.lineList.length == 0" style="background-color:DeepPink; color:black;" class="mx-1">Floral</b-badge>
                                    <div v-for="line in perfume.lineList" :key="line.id">
                                        <b-badge v-if="line == 'Floral'" style="background-color:DeepPink; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Citrus'" style="background-color:Yellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Chypre'" style="background-color:DeepSkyBlue; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Oriental'" style="background-color:peru; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Fruity'" style="background-color:OrangeRed; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Woody'" style="background-color:BurlyWood; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Green'" style="background-color:GreenYellow; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aldehyde'" style="background-color:LavenderBlush; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Spicy'" style="background-color:FireBrick; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Gourmand'" style="background-color:Chocolate; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Musk'" style="background-color:BlueViolet; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Vanilla'" style="background-color:Beige; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Leather'" style="background-color:SaddleBrown; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aromatic'" style="background-color:Plum; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Aquatic'" style="background-color:Aqua; color:black" class="mx-1">{{line}}</b-badge>
                                        <b-badge v-if="line == 'Cotton'" style="background-color:Azure; color:black" class="mx-1">{{line}}</b-badge>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import constants from '../lib/constants';

export default {
    data() {
        return {
            username:'',
            byAgePerfume: [],
            newStudentMen : [],
            newStudentWomen : [],
            socialMen : [],
            socialWomen : [],
            thirtyMen : [],
            thirtyWomen : [],
            fortyMen : [],
            fortyWomen : [],
            fiftyMen : [],
            fiftyWomen : [],
            springPerfume : [],
            summerPerfume : [],
            autumnPerfume : [],
            winterPerfume : [],
            flag : 0,
        }
    },
    methods: {
        getUser(){
            axios.get(`${constants.SERVER_URL}/api/accounts/userdetail/${this.$cookies.get('email')}/`)
            .then((res)=>{
                this.username = res.data.username
            }).catch((err)=>console.log(err))
        },
        getByAgePerfume() {
            axios.get(`${constants.SERVER_URL}/api/perfumes/recommend/age/`)
            .then((res)=>{
                this.newStudentMen = res.data.newmen
                this.newStudentWomen = res.data.newwomen
                this.socialMen = res.data.socialmen
                this.socialWomen = res.data.socialwomen
                this.thirtyMen = res.data.thirtymen
                this.thirtyWomen = res.data.thirtywomen
                this.fortyMen = res.data.fortymen
                this.fortyWomen = res.data.fortywomen
                this.fiftyMen = res.data.fiftymen
                this.fiftyWomen = res.data.fiftywomen
            })
            .catch((err)=>{console.log(err)})
        },
        getWeather() {
            axios.get(`${constants.SERVER_URL}/api/perfumes/recommend/weather/`)
            .then((res)=>{
                this.springPerfume = res.data.spring
                this.summerPerfume = res.data.summer
                this.autumnPerfume = res.data.autumn
                this.winterPerfume = res.data.winter
            })
            .catch((err)=>{console.log(err)})
        },
        goDetail(id) {
            this.$router.push(`/perfumedetail/${id}`).catch(() => {
                this.$router.go()          
            })
        },
        goMain() {
            this.$router.push('/').catch(() => {
                this.$router.go()
            })
        },

        giveFlag(num){
            if (this.flag == num) {
                this.flag = 0
            } else {
                this.flag = num
        }
    }

    },
    created(){
        this.getUser()
        this.getByAgePerfume()
        this.getWeather()
    },
}
</script>

<style scoped>
.latestbtn {
  background-color: white;
  color:crimson;
}
.latestbtn:hover {
  background-color: crimson;
  color:white;
}
.latestbtn:active {
  background-color: yellow;
  color:white;
}

.property-card
{
  height:18em;
  width:14em;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
  -ms-flex-direction:column;
  flex-direction:column;
  position:relative;
  -webkit-transition:all 0.4s cubic-bezier(0.645, 0.045, 0.355, 1);
  -o-transition:all 0.4s cubic-bezier(0.645, 0.045, 0.355, 1);
  transition:all 0.4s cubic-bezier(0.645, 0.045, 0.355, 1);
  border-radius:30px;
  overflow:hidden;
  -webkit-box-shadow:  15px 15px 27px #e1e1e3, -15px -15px 27px #ffffff;
  box-shadow:  15px 15px 27px #e1e1e3
}
/* ^-- The margin bottom is necessary for the drop shadow otherwise it gets clipped in certain cases. */

/* Top Half of card, image. */

.property-image
{
  height:18em;
  width:14rem;
  padding:0;
  position:Absolute;
  /* top:0px; */
  -webkit-transition:all 0.4s cubic-bezier(0.645, 0.045, 0.355, 1);
  -o-transition:all 0.4s cubic-bezier(0.645, 0.045, 0.355, 1);
  transition:all 0.4s cubic-bezier(0.645, 0.045, 0.355, 1);
  /* background-image:url('https://cdn.photographylife.com/wp-content/uploads/2017/01/What-is-landscape-photography.jpg'); */
  background-size:cover;
  background-position: center;
  background-repeat:no-repeat;
}

/* Bottom Card Section */

.property-description
{
  background-color: rgba(50, 50, 50, 0.9);
  color:white;
  height:10em;
  width:14em;
  position:absolute;
  bottom:0em;
  -webkit-transition:all 0.4s cubic-bezier(0.645, 0.045, 0.355, 1);
  -o-transition:all 0.4s cubic-bezier(0.645, 0.045, 0.355, 1);
  transition:all 0.4s cubic-bezier(0.645, 0.045, 0.355, 1);
  padding: 0.5em 1em;
  text-align:center;
}
/* Property Cards Hover States */

.property-card:hover .property-description
{
  height:0em;
  padding:0px 1em;
}
.property-card:hover .property-image
{
  height:18em;
}

.property-card:hover .property-social-icons
{
  background-color:white;
}

.property-card:hover .property-social-icons:hover
{
  background-color:blue;
  cursor:pointer;
}



.img-img{width: 100%; }
        .imgHoverEvent{position: relative; overflow: hidden; display: inline-block;}
        .imgHoverEvent .imgBox{text-align: center; background-size: auto 100%;}
        .imgHoverEvent .hoverBox{position: absolute; width: 100%; height: 100%;}
        .hoverBox p.p1{text-align:center; font-size:18px;}
        .hoverBox p.p2{text-align:center; margin-top: 40px;}
        .event1 .hoverBox{background: linear-gradient(to bottom, rgba(0,0,0,0) 5%,rgb(15, 15, 15) 90%); transform: translateY(75%); transition: 0.5s;}
        .event1:hover .hoverBox{transform: translateY(0);}

        .event2 .imgBox{filter: blur(0)}
        .event2:hover .imgBox{filter: blur(5px) grayscale(100%); transition: 0.5s;}
        .event2 .hoverBox .movie-text {visibility: hidden; }
        .event2:hover .hoverBox .movie-text {visibility: visible;}
</style>