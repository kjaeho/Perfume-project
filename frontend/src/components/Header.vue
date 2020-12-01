<template>
  <div v-if="isHeader" class="body" style="padding-left:0; margin-left:0; width:100%">

    <!-- sidebar left align -->
    <nav class="navbar bg-light" style="overflow-y:hidden; overflow-x:hidden; z-index:5;">
      <ul class="navbar-nav" style="">
        <li class="logo">
          <a @click="goMain" class="nav-link" style="cursor:pointer; background-color:lightgray">
            <span class="link-text logo-text" style="font-family: 'Black Han Sans', sans-serif; color:deeppink;">Triple'S</span>
            <svg
              aria-hidden="true"
              focusable="false"
              data-prefix="fad"
              data-icon="angle-double-right"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 448 512"
              class="svg-inline--fa fa-angle-double-right fa-w-14 fa-5x"
            >
              <g class="fa-group">
                <path
                  fill="currentColor"
                  d="M224 273L88.37 409a23.78 23.78 0 0 1-33.8 0L32 386.36a23.94 23.94 0 0 1 0-33.89l96.13-96.37L32 159.73a23.94 23.94 0 0 1 0-33.89l22.44-22.79a23.78 23.78 0 0 1 33.8 0L223.88 239a23.94 23.94 0 0 1 .1 34z"
                  class="fa-secondary"
                ></path>
                <path
                  fill="currentColor"
                  d="M415.89 273L280.34 409a23.77 23.77 0 0 1-33.79 0L224 386.26a23.94 23.94 0 0 1 0-33.89L320.11 256l-96-96.47a23.94 23.94 0 0 1 0-33.89l22.52-22.59a23.77 23.77 0 0 1 33.79 0L416 239a24 24 0 0 1-.11 34z"
                  class="fa-secondary"
                ></path>
              </g>
            </svg>
          </a>
        </li>
        <!-- Home button -->
        <li class="nav-item" style="cursor:pointer;" @click="goMain">
          <a class="nav-link">
            <svg 
                xmlns="http://www.w3.org/2000/svg"
                id="Outline" 
                viewBox="0 0 512 512" 
                width="512" 
                height="512"
                >
                <path
                    fill="currentColor"
                    class="fa-secondary"
                    d="M471.982,417.008Q472,416.5,472,416a32.036,32.036,0,0,0-32-32V236l28.8-21.6a8,8,0,0,0-.08-12.859L400,151.322V64a8,8,0,0,0,8-8V24a8,8,0,0,0-8-8H320a8,8,0,0,0-8,8V56a8,8,0,0,0,8,8V92.861l-59.28-43.32a8,8,0,0,0-9.44,0l-208,152A8,8,0,0,0,43.2,214.4L72,236V384a32.036,32.036,0,0,0-32,32q0,.5.018,1.008A32,32,0,0,0,48,480H464a32,32,0,0,0,7.982-62.992ZM328,32h64V48H328Zm8,72V64h48v75.63L335.243,104ZM256,65.908,450.555,208.084l-18.628,13.971L260.706,97.53a8,8,0,0,0-9.412,0L80.073,222.055,61.445,208.084ZM32,448a16.019,16.019,0,0,1,15.76-16l.019,0c.409.057.818.106,1.235.133a8,8,0,0,0,8.023-10.716A15.727,15.727,0,0,1,56,416a16.019,16.019,0,0,1,16-16v64H48A16.019,16.019,0,0,1,32,448Zm344,16H280V288h96Zm16,0V280a8,8,0,0,0-8-8H272a8,8,0,0,0-8,8V464H88V236.074L256,113.892,424,236.074V464Zm72,0H440V400a16.019,16.019,0,0,1,16,16,15.727,15.727,0,0,1-1.037,5.421,8,8,0,0,0,8.023,10.716c.417-.027.826-.076,1.235-.133l.019,0a16,16,0,0,1-.24,32Z"
                />
                <path 
                    fill="currentColor"
                    class="fa-primary"
                    d="M224,272H128a8,8,0,0,0-8,8V392a8,8,0,0,0,8,8h96a8,8,0,0,0,8-8V280A8,8,0,0,0,224,272Zm-8,56H184V288h32Zm-48-40v40H136V288Zm-32,56h32v40H136Zm48,40V344h32v40Z"
                />
                <circle 
                    cx="304" 
                    cy="368" 
                    r="8" 
                    transform="translate(-152.323 508.032) rotate(-67.5)"
                />
            </svg>

            <!-- <svg
              aria-hidden="true"
              focusable="false"
              data-prefix="fas" 
              data-icon="home" 
              class="svg-inline--fa fa-home fa-w-18" 
              role="img" xmlns="http://www.w3.org/2000/svg" 
              viewBox="0 0 576 512">
              <path 
                fill="currentColor" 
                d="M280.37 148.26L96 300.11V464a16 16 0 0 0 16 16l112.06-.29a16 16 0 0 0 15.92-16V368a16 16 0 0 1 16-16h64a16 16 0 0 1 16 16v95.64a16 16 0 0 0 16 16.05L464 480a16 16 0 0 0 16-16V300L295.67 148.26a12.19 12.19 0 0 0-15.3 0zM571.6 251.47L488 182.56V44.05a12 12 0 0 0-12-12h-56a12 12 0 0 0-12 12v72.61L318.47 43a48 48 0 0 0-61 0L4.34 251.47a12 12 0 0 0-1.6 16.9l25.5 31A12 12 0 0 0 45.15 301l235.22-193.74a12.19 12.19 0 0 1 15.3 0L530.9 301a12 12 0 0 0 16.9-1.6l25.5-31a12 12 0 0 0-1.7-16.93z"
                class="fa-secondary"
                >
              </path>
            </svg> -->
            <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;">Home</span>
          </a>
        </li>
        <!-- recommend button -->
        <li class="nav-item" style="cursor:pointer" @click="goRecommend">
          <a class="nav-link">
            <svg 
              height="512" 
              viewBox="0 0 64 64" 
              width="512" 
              xmlns="http://www.w3.org/2000/svg">
              <path class="fa-primary" fill="currentColor" d="m50 15h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m54 15h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m52 13h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m52 17h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m56 21h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m60 21h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m58 19h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m58 23h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m42 15h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m38 15h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m40 13h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m40 17h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m36 21h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m32 21h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m34 19h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m34 23h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m63.339 31.691a1 1 0 0 0 -.951-.691h-11.029l-3.408-10.489a1 1 0 0 0 -1.9 0l-3.41 10.489h-11.029a1 1 0 0 0 -.588 1.809l8.922 6.483-3.408 10.489a1 1 0 0 0 1.539 1.119l8.923-6.483 8.923 6.483a1 1 0 0 0 1.539-1.118l-3.408-10.49 8.922-6.483a1 1 0 0 0 .363-1.118zm-11.049 6.409a1 1 0 0 0 -.363 1.118l2.681 8.253-7.02-5.1a1 1 0 0 0 -1.176 0l-7.02 5.1 2.681-8.253a1 1 0 0 0 -.363-1.118l-7.021-5.1h8.678a1 1 0 0 0 .951-.691l2.682-8.253 2.682 8.253a1 1 0 0 0 .951.691h8.678z"/>
              <path class="fa-secondary" fill="currentColor" d="m50 54h-17.649l-7.5-6h6.149a3 3 0 0 0 3-3v-.171a2.98 2.98 0 0 0 -.879-2.122l-1.513-1.507-6.94-6.067a2.988 2.988 0 0 0 -3.315-.424l-7.353 3.673v-.382a1 1 0 0 0 -1-1h-4a1 1 0 0 0 -1 1v.382l-4.553-2.282a1 1 0 0 0 -1.447.9v18a1 1 0 0 0 1.447.9l4.553-2.282v.382a1 1 0 0 0 1 1h4a.993.993 0 0 0 .93-.656l6.483 6.483a3.98 3.98 0 0 0 2.832 1.173h26.755a4 4 0 0 0 0-8zm-46-.618v-14.764l4 2v10.764zm8-.382h-2v-14h2zm38 7h-26.755a1.991 1.991 0 0 1 -1.418-.587l-7.827-7.827v-10.968l8.247-4.123a.993.993 0 0 1 1.105.141l6.891 6.021 1.464 1.464a1 1 0 0 1 .293.708v.171a1 1 0 0 1 -1 1h-9a1 1 0 0 0 -.625 1.781l10 8a1 1 0 0 0 .625.219h18a2 2 0 0 1 0 4z"/>
              <path class="fa-secondary" fill="currentColor" d="m5 44h2v4h-2z"/>
              <path class="fa-secondary" fill="currentColor" d="m14.049 19.219-1.229 3.781h-3.975a1 1 0 0 0 -.588 1.809l3.216 2.337-1.228 3.781a1 1 0 0 0 1.539 1.118l3.216-2.337 3.216 2.337a1 1 0 0 0 1.539-1.118l-1.228-3.781 3.216-2.337a1 1 0 0 0 -.588-1.809h-3.975l-1.229-3.781a1 1 0 0 0 -1.9 0zm2.404 5.781h1.625l-1.315.955a1 1 0 0 0 -.363 1.118l.5 1.545-1.314-.955a1 1 0 0 0 -1.176 0l-1.314.955.5-1.545a1 1 0 0 0 -.363-1.118l-1.311-.955h1.625a1 1 0 0 0 .951-.691l.5-1.545.5 1.545a1 1 0 0 0 .955.691z"/>
              <path class="fa-secondary" fill="currentColor" d="m21.473 13.146-1.228 3.781a1 1 0 0 0 1.539 1.118l3.216-2.337 3.216 2.337a1 1 0 0 0 1.539-1.118l-1.228-3.781 3.216-2.337a1 1 0 0 0 -.588-1.809h-3.975l-1.229-3.781a1 1 0 0 0 -1.9 0l-1.231 3.781h-3.975a1 1 0 0 0 -.588 1.809zm2.074-2.146a1 1 0 0 0 .951-.691l.502-1.545.5 1.545a1 1 0 0 0 .951.691h1.625l-1.315.955a1 1 0 0 0 -.363 1.118l.5 1.545-1.314-.955a1 1 0 0 0 -1.176 0l-1.314.955.5-1.545a1 1 0 0 0 -.363-1.118l-1.309-.955z"/>
              <path class="fa-secondary" fill="currentColor" d="m3.245 13.927a1 1 0 0 0 1.539 1.118l3.216-2.337 3.216 2.337a1 1 0 0 0 1.539-1.118l-1.228-3.781 3.216-2.337a1 1 0 0 0 -.588-1.809h-3.975l-1.229-3.781a1 1 0 0 0 -1.9 0l-1.231 3.781h-3.975a1 1 0 0 0 -.588 1.809l3.216 2.337zm3.302-5.927a1 1 0 0 0 .953-.691l.5-1.545.5 1.545a1 1 0 0 0 .953.691h1.625l-1.315.955a1 1 0 0 0 -.363 1.118l.5 1.545-1.314-.955a1 1 0 0 0 -1.176 0l-1.31.955.5-1.545a1 1 0 0 0 -.363-1.118l-1.315-.955z"/>
            </svg>
            <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;">Recommend</span>
          </a>
        </li>
        <!-- Perfume list button -->
        <li class="nav-item">
          <a @click="goPerfume" class="nav-link" style="cursor:pointer">
            <svg 
                height="480pt" 
                viewBox="-52 0 480 480" 
                width="480pt" 
                xmlns="http://www.w3.org/2000/svg"
                >
                <path
                    fill="currentColor"
                    d="m168 40h-64c-4.417969 0-8 3.582031-8 8v88h-24c-4.417969 0-8 3.582031-8 8v40h-8c-2.335938 0-4.550781 1.019531-6.070312 2.792969l-48 56c-1.625 1.894531-2.273438 4.4375-1.753907 6.878906l48 224c.789063 3.691406 4.050781 6.328125 7.824219 6.328125h160c3.773438 0 7.035156-2.636719 7.824219-6.328125l48-224c.523437-2.441406-.125-4.984375-1.75-6.878906l-48-56c-1.523438-1.773438-3.738281-2.792969-6.074219-2.792969h-8v-40c0-4.417969-3.582031-8-8-8h-24v-88c0-4.417969-3.582031-8-8-8zm-56 16h48v32h-16v16h16v32h-48zm134.609375 184h-22.609375v16h30.105469l-18.855469 88h-179.25v16h175.816406l-22.289062 104h-147.054688l-3.433594-16h132.960938v-16h-36.457031l19.953125-53.191406-14.992188-5.601563-22.046875 58.792969h-4.914062l-22.046875-58.808594-14.992188 5.601563 19.953125 53.207031h-60.847656l-37.714844-176h30.105469v-16h-22.609375l34.289063-40h30.535156l-25.160156 44c-.984376 1.726562-1.292969 3.761719-.863282 5.703125l16 72 15.617188-3.472656-15.328125-68.941407 28.160156-49.289062h54.71875l28.160156 49.289062-15.328125 68.976563 15.617188 3.46875 16-72c.429687-1.941406.125-3.976563-.863282-5.703125l-25.160156-44.03125h30.535156zm-54.609375-56h-112v-32h112zm0 0"
                    class="fa-secondary"
                />
                <path
                    fill="currentColor"
                    d="m358.617188 59.152344c.910156-3.648438 1.375-7.394532 1.382812-11.152344 0-26.507812-21.488281-48-48-48-26.507812 0-48 21.492188-48 48h16c-.113281-12.898438 7.53125-24.605469 19.386719-29.691406 11.855469-5.082032 25.605469-2.550782 34.871093 6.421875 9.269532 8.972656 12.242188 22.632812 7.542969 34.644531-1.351562 3.554688-.011719 7.566406 3.199219 9.601562 9.328125 5.804688 15 16.011719 15 27 0 10.988282-5.671875 21.195313-15 27-3.210938 2.03125-4.550781 6.046876-3.199219 9.597657 4.574219 11.972656 1.550781 25.515625-7.671875 34.40625-9.226562 8.894531-22.871094 11.417969-34.664062 6.410156-11.792969-5.007813-19.457032-16.578125-19.464844-29.390625h-16c0 26.507812 21.492188 48 48 48 26.511719 0 48-21.492188 48-48-.007812-3.757812-.472656-7.503906-1.382812-11.152344 11.007812-9.070312 17.382812-22.585937 17.382812-36.847656s-6.375-27.777344-17.382812-36.847656zm0 0"
                    class="fa-primary"
                />
                <path
                    fill="currentColor"
                    d="m208 88h40v16h-40zm0 0"
                    class="fa-secondary"
                />
                <path
                    fill="currentColor"
                    d="m264 88h16v16h-16zm0 0"
                    class="fa-secondary"
                />
                <path
                    fill="currentColor"
                    d="m214.058594 56.238281 32-8 3.878906 15.523438-31.996094 8zm0 0"
                    class="fa-secondary"
                />
                <path
                    fill="currentColor"
                    d="m214.058594 135.757812 3.878906-15.523437 32 8-3.882812 15.523437zm0 0"
                    class="fa-secondary"
                />
                <path
                    fill="currentColor"
                    d="m104 240h64v16h-64zm0 0"
                    class="fa-secondary"
                />
            </svg>
            <!-- <svg 
              aria-hidden="true" 
              focusable="false" 
              data-prefix="fas" 
              data-icon="film" 
              class="svg-inline--fa fa-film fa-w-16" 
              role="img" 
              xmlns="http://www.w3.org/2000/svg" 
              viewBox="0 0 512 512">
              <path 
              fill="currentColor" 
              d="M488 64h-8v20c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12V64H96v20c0 6.6-5.4 12-12 12H44c-6.6 0-12-5.4-12-12V64h-8C10.7 64 0 74.7 0 88v336c0 13.3 10.7 24 24 24h8v-20c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v20h320v-20c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v20h8c13.3 0 24-10.7 24-24V88c0-13.3-10.7-24-24-24zM96 372c0 6.6-5.4 12-12 12H44c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40zm0-96c0 6.6-5.4 12-12 12H44c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40zm0-96c0 6.6-5.4 12-12 12H44c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40zm272 208c0 6.6-5.4 12-12 12H156c-6.6 0-12-5.4-12-12v-96c0-6.6 5.4-12 12-12h200c6.6 0 12 5.4 12 12v96zm0-168c0 6.6-5.4 12-12 12H156c-6.6 0-12-5.4-12-12v-96c0-6.6 5.4-12 12-12h200c6.6 0 12 5.4 12 12v96zm112 152c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40zm0-96c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40zm0-96c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40z"
              class="fa-secondary"
              >
              </path>
            </svg> -->
            <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;">Perfume</span>
          </a>
        </li>

       <!-- Login -->
        <li v-if="!isLoggedIn" class="nav-item" style="cursor:pointer" data-toggle="modal" data-target="#Login">
          <a class="nav-link">
            <svg 
                height="500pt" 
                viewBox="-48 0 500 500.40043" 
                width="500pt" 
                xmlns="http://www.w3.org/2000/svg"
                >
                <path
                    fill="currentColor"
                    class="fa-primary" 
                    d="m6.722656 406h152.199219c14.011719 55.441406 63.851563 94.316406 121.039063 94.402344 68.765624 0 124.714843-56.0625 124.714843-124.832032 0-68.765624-55.945312-124.769531-124.710937-124.769531-7.613282-.011719-15.214844.675781-22.703125 2.046875-13.808594-48.289062-57.863281-81.644531-108.085938-81.847656h-36.808593c-62.09375.175781-112.3007818 50.636719-112.167969 112.730469v114.808593c0 3.863282 2.660156 7.460938 6.523437 7.460938zm383.953125-30.542969c0 61.144531-49.566406 110.714844-110.710937 110.714844-61.148438 0-110.714844-49.570313-110.714844-110.714844s49.566406-110.714843 110.714844-110.714843c61.117187.070312 110.644531 49.597656 110.710937 110.714843zm-376.476562-91.683593c-.15625-54.382813 43.796875-98.601563 98.179687-98.773438h36.785156c43.746094.191406 82.175782 29.089844 94.5 71.066406-52.503906 16.160156-88.351562 64.648438-88.410156 119.585938.023438 5.464844.367188 10.921875 1.03125 16.347656h-142.085937zm0 0"
                />
                <path
                    fill="currentColor"
                    class="fa-primary" 
                    d="m130.652344 157h.039062v-6.777344l.070313 7.113282c43.496093-.050782 78.730469-35.324219 78.738281-78.820313-.019531-20.875-8.339844-40.882813-23.132812-55.613281-14.792969-14.730469-34.835938-22.9726565-55.710938-22.902344h-.035156c-43.355469.0078125-78.492188 35.164062-78.484375 78.515625.007812 43.355469 35.164062 78.492187 78.515625 78.484375zm-45.820313-124.089844c12.140625-12.1875 28.65625-18.996094 45.859375-18.910156h.027344c35.625-.007812 64.507812 28.859375 64.519531 64.484375.007813 35.621094-28.863281 64.507813-64.484375 64.515625h-.097656c-26.148438.132812-49.78125-15.542969-59.828125-39.679688-10.046875-24.140624-4.515625-51.957031 14.003906-70.410156zm0 0"
                />
                <path
                    fill="currentColor"
                    class="fa-secondary" 
                    d="m208.800781 448.699219c1.855469.003906 3.636719-.734375 4.949219-2.050781l6.101562-6.097657 17.675782 17.527344c2.726562 2.710937 7.132812 2.710937 9.859375 0l25.222656-25.035156c1.320313-1.308594 2.066406-3.09375 2.070313-4.953125.003906-1.863282-.734376-3.648438-2.050782-4.964844l-17.675781-17.675781 37.316406-37.316407c17.363281 12.222657 41.191407 9.132813 54.859375-7.113281 13.671875-16.25 12.636719-40.253906-2.375-55.269531-15.015625-15.015625-39.023437-16.046875-55.269531-2.378906-16.25 13.671875-19.339844 37.5-7.113281 54.863281l-78.523438 78.519531c-2.003906 2.003906-2.601562 5.011719-1.519531 7.628906 1.085937 2.617188 3.636719 4.320313 6.46875 4.320313zm48.964844-20.648438-15.308594 15.195313-12.699219-12.601563 15.296876-15.300781zm58-120.15625c14.824219.003907 26.84375 12.023438 26.84375 26.847657 0 14.824218-12.019531 26.84375-26.847656 26.84375-14.824219 0-26.84375-12.019532-26.84375-26.84375.019531-14.816407 12.023437-26.820313 26.839843-26.839844zm0 0"
                />
            </svg>
            
            <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;">Login</span>
          </a>
        </li>

        <!-- profile -->
        <li v-if="isLoggedIn" class="nav-item">
          <a @click="goProfile" class="nav-link" style="cursor:pointer">
            <svg 
              id="Capa_1" 
              enable-background="new 0 0 512 512" 
              height="512" 
              viewBox="0 0 512 512" 
              width="512" 
              xmlns="http://www.w3.org/2000/svg"
              >
              <g>
                <path
                  fill="currentColor"
                  d="m308.5 512h-255c-12.407 0-22.5-10.094-22.5-22.5v-375.3c0-12.406 10.093-22.5 22.5-22.5h43.11c4.142 0 7.5 3.357 7.5 7.5s-3.358 7.5-7.5 7.5h-43.11c-4.136 0-7.5 3.364-7.5 7.5v375.3c0 4.136 3.364 7.5 7.5 7.5h255c4.136 0 7.5-3.364 7.5-7.5v-174.5h-172.5c-12.407 0-22.5-10.094-22.5-22.5v-270c0-12.406 10.093-22.5 22.5-22.5h225c12.407 0 22.5 10.094 22.5 22.5v75c0 4.143-3.358 7.5-7.5 7.5s-7.5-3.357-7.5-7.5v-75c0-4.136-3.364-7.5-7.5-7.5h-225c-4.136 0-7.5 3.364-7.5 7.5v270c0 4.136 3.364 7.5 7.5 7.5h225c4.136 0 7.5-3.364 7.5-7.5v-165c0-4.143 3.358-7.5 7.5-7.5h45c4.142 0 7.5 3.357 7.5 7.5s-3.358 7.5-7.5 7.5h-37.5v30h37.5c4.142 0 7.5 3.357 7.5 7.5s-3.358 7.5-7.5 7.5h-37.5v30h37.5c4.142 0 7.5 3.357 7.5 7.5s-3.358 7.5-7.5 7.5h-37.5v30h37.5c4.142 0 7.5 3.357 7.5 7.5s-3.358 7.5-7.5 7.5h-37.5v22.5c0 2.628-.453 5.153-1.285 7.5h38.785c4.142 0 7.5 3.357 7.5 7.5s-3.358 7.5-7.5 7.5h-97.5v30h97.5c4.142 0 7.5 3.357 7.5 7.5s-3.358 7.5-7.5 7.5h-97.5v47h127.5c4.136 0 7.5-3.364 7.5-7.5v-330.3c0-4.136-3.364-7.5-7.5-7.5h-45c-4.142 0-7.5-3.357-7.5-7.5s3.358-7.5 7.5-7.5h45c12.407 0 22.5 10.094 22.5 22.5v330.3c0 12.406-10.093 22.5-22.5 22.5h-127.5v45h82.5c4.136 0 7.5-3.364 7.5-7.5v-15c0-4.143 3.358-7.5 7.5-7.5s7.5 3.357 7.5 7.5v15c0 12.406-10.093 22.5-22.5 22.5h-82.5v7.5c0 12.406-10.093 22.5-22.5 22.5zm45-227h-195c-4.142 0-7.5-3.357-7.5-7.5v-26.054c0-38.539 25.48-47.357 44.085-53.796 15.355-5.314 24.074-8.894 25.611-20.443-16.552-11.308-27.437-30.326-27.437-51.841v-30.926c0-34.595 28.146-62.74 62.741-62.74s62.741 28.146 62.741 62.74v30.926c0 21.515-10.884 40.533-27.437 51.841 1.537 11.55 10.256 15.129 25.611 20.443 18.605 6.439 44.085 15.257 44.085 53.796v26.054c0 4.143-3.358 7.5-7.5 7.5zm-187.5-15h180v-18.554c0-27.857-15.752-33.309-33.991-39.621-13.47-4.661-29.709-10.283-34.534-27.505-6.703 2.45-13.935 3.786-21.475 3.786s-14.772-1.336-21.475-3.786c-4.825 17.222-21.064 22.844-34.534 27.505-18.239 6.313-33.991 11.764-33.991 39.621zm90-223.3c-26.324 0-47.741 21.416-47.741 47.74v30.926c0 26.324 21.417 47.74 47.741 47.74s47.741-21.416 47.741-47.74v-30.926c0-26.324-21.417-47.74-47.741-47.74z"
                  class="fa-secondary"
                />
              </g>
            </svg>
            <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;">Profile</span>
          </a>
        </li>

        <!-- photo upload -->
        <li v-if="isLoggedIn" class="nav-item">
          <a class="nav-link" style="cursor:pointer" data-toggle="modal" data-target="#upload" >
            <svg 
              id="Capa_1" 
              enable-background="new 0 0 512.112 512.112" 
              height="512" 
              viewBox="0 0 512.112 512.112" 
              width="512" 
              xmlns="http://www.w3.org/2000/svg"
              >
              <g>
                <path 
                  fill="currentColor"
                  class="fa-secondary"
                  d="m448.042 499.019-87.247-87.247c-37.471-47.749 25.152-76.421-21.384-177.42-8.146-23.162-18.803-53.441-18.859-53.6-5.95-16.901-17.224-31.524-31.965-41.61l.01-89.823v-.003c0-21.706-16.673-39.365-37.168-39.365h-152.354c-20.495 0-37.168 17.659-37.168 39.365v56.554c0 4.2 3.404 7.604 7.604 7.604s7.604-3.404 7.604-7.604v-24.707h196.264v242.569l-34.945-21.779v-41.953c0-24.804-14.374-46.305-35.225-56.639 11.056-7.58 18.903-19.516 21.036-33.316h25.553c4.2 0 7.604-3.404 7.604-7.604s-3.404-7.604-7.604-7.604h-25.553c-3.67-23.745-24.246-41.982-49.003-41.982s-45.333 18.237-49.003 41.982h-25.553c-4.2 0-7.604 3.404-7.604 7.604s3.404 7.604 7.604 7.604h25.553c2.134 13.804 9.984 25.743 21.046 33.323-20.843 10.336-35.211 31.833-35.211 56.632v78.159h-34.959v-190.638c0-4.2-3.404-7.604-7.604-7.604s-7.604 3.404-7.604 7.604v223.842c0 21.706 16.673 39.365 37.168 39.365h29.187c7.195 15.196 19.467 27.247 35.051 34.237 49.127 20.677 55.751 38.353 88.34 65.082 1.242 3.291 26.806 1.559 29.341 1.952 4.199 0 7.604-3.404 7.604-7.604s-3.404-7.604-7.604-7.604h-21.334l-47.297-42.58c2.19-3.843-57.672-24.765-66.726-43.483 0 0 108.111-.065 109.255-.177l16.262 15.052c7.179 6.644 17.537-4.49 10.331-11.16l-18.955-17.545c-.001-.001-.003-.002-.004-.003l-84.122-77.831c-6.053-6.153-5.909-16.16.148-22.217 6.34-6.341 14.434-5.319 21.436-.936l75.814 47.251c4.758 4.44 12.786.952 12.786-5.554v-178.98c7.888 7.499 13.973 16.815 17.619 27.173 6.372 20.07 32.466 86.207 34.507 105.834 10.097 56.908-28.857 92.37 9.328 130.891l74.267 74.266h-107.365c-4.199 0-7.604 3.404-7.604 7.604s3.404 7.604 7.604 7.604h125.721c6.62 0 10.061-8.296 5.377-12.981zm-370.927-433.064v-16.64c0-13.321 9.851-24.157 21.96-24.157h152.354c12.108 0 21.959 10.837 21.96 24.155l-.007 16.642zm98.128 62.108c16.343 0 30.049 11.466 33.52 26.774h-67.041c3.471-15.308 17.178-26.774 33.521-26.774zm33.52 41.982c-3.471 15.308-17.177 26.774-33.52 26.774s-30.049-11.466-33.521-26.774zm-109.688 225.476c-12.109 0-21.96-10.837-21.96-24.157v-17.997l115.969.002 45.563 42.152zm90.609-118.568c-16.474 0-30.562 13.794-31.006 30.235-.38 14.063 8.575 22.278 17.968 30.971h-49.365v-78.159c0-26.452 21.52-47.972 47.972-47.972 26.451 0 47.972 21.52 47.972 47.972v32.475c-10.195-6.356-21.036-15.522-33.541-15.522z"
                />
                <path 
                  fill="currentColor"
                  class="fa-secondary"
                  d="m156.159 366.524c-4.2 0-7.604 3.404-7.604 7.604s3.404 7.604 7.604 7.604h38.188c4.2 0 7.604-3.404 7.604-7.604s-3.404-7.604-7.604-7.604z"
                />
                <path 
                  fill="currentColor"
                  class="fa-secondary"
                  d="m188.885 37.953h-27.284c-4.2 0-7.604 3.404-7.604 7.604s3.404 7.604 7.604 7.604h27.284c4.2 0 7.604-3.404 7.604-7.604s-3.405-7.604-7.604-7.604z"
                />
                <path 
                  fill="currentColor"
                  class="fa-secondary"
                  d="m230.831 37.479c-4.461 0-8.078 3.616-8.078 8.077s3.616 8.078 8.078 8.078c4.461 0 8.078-3.617 8.078-8.078s-3.617-8.077-8.078-8.077z"
                />
                <path 
                  fill="currentColor"
                  class="fa-secondary"
                  d="m313.44 27.668c1.959 0 3.918-.752 5.405-2.255l12.33-12.459c2.954-2.985 2.929-7.799-.056-10.753-2.984-2.953-7.799-2.93-10.753.056l-12.33 12.459c-4.645 4.692-1.205 12.952 5.404 12.952z"
                />
                <path 
                  fill="currentColor"
                  class="fa-secondary"
                  d="m320.366 88.857c6.9 6.974 17.707-3.727 10.81-10.697l-12.331-12.46c-2.954-2.986-7.769-3.009-10.753-.056-2.985 2.954-3.01 7.768-.056 10.753z"
                />
                <path 
                  fill="currentColor"
                  class="fa-secondary"
                  d="m318.166 45.557c0 4.2 3.404 7.604 7.604 7.604h17.727c4.2 0 7.604-3.404 7.604-7.604s-3.404-7.604-7.604-7.604h-17.727c-4.199 0-7.604 3.404-7.604 7.604z"
                />
              </g>
            </svg>
            <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;">Upload</span>
          </a>
        </li>


        <!-- 로그아웃 -->
        <li v-if="isLoggedIn" class="nav-item" style="cursor:pointer" @click="logout">
          <a class="nav-link">
            <svg 
              id="Layer_1" 
              height="512" 
              viewBox="0 0 128 128" 
              width="512" 
              xmlns="http://www.w3.org/2000/svg" 
              data-name="Layer 1"
              >
              <path
                fill="currentColor"
                class="fa-secondary" 
                d="m13.076 97.083a1.75 1.75 0 0 0 1.75-1.75v-28.666a1.75 1.75 0 0 0 -3.5 0v28.666a1.75 1.75 0 0 0 1.75 1.75z"
              />
              <path
                fill="currentColor"
                class="fa-secondary" 
                d="m122.38 64.97c.027-.041.046-.085.069-.128a1.037 1.037 0 0 0 .146-.348c.015-.051.035-.1.045-.152a1.755 1.755 0 0 0 0-.685c-.01-.053-.03-.1-.045-.152a1.733 1.733 0 0 0 -.054-.174 1.692 1.692 0 0 0 -.092-.174c-.023-.042-.042-.086-.069-.127a1.75 1.75 0 0 0 -.22-.269l-12.509-12.509a1.75 1.75 0 0 0 -2.475 2.475l9.524 9.523h-53.276a1.75 1.75 0 0 0 0 3.5h53.276l-9.523 9.523a1.75 1.75 0 1 0 2.475 2.475l12.508-12.509a1.75 1.75 0 0 0 .22-.269z"
              />
              <path
                fill="currentColor"
                class="fa-secondary"  
                d="m95.424 72.25a1.75 1.75 0 0 0 -1.75 1.75v36.9h-45.041v-93.8h45.041v36.9a1.75 1.75 0 1 0 3.5 0v-38.65a1.75 1.75 0 0 0 -1.75-1.75h-46.791v-7.1a1.75 1.75 0 0 0 -2.461-1.6l-39.807 17.693a1.751 1.751 0 0 0 -1.039 1.6v79.615a1.751 1.751 0 0 0 1.039 1.6l39.807 17.692a1.75 1.75 0 0 0 2.461-1.6v-7.1h46.791a1.75 1.75 0 0 0 1.75-1.75v-38.65a1.75 1.75 0 0 0 -1.75-1.75zm-50.291 46.558-36.307-16.138v-77.34l36.307-16.138z"
              />
            </svg>
            
            <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;">Logout</span>
          </a>
        </li>


        <li class="nav-item" id="themeButton" style="">
          <!-- <a class="nav-link" style="cursor:pointer"> -->
          <a class="">
            <!-- 화면 보호 모드 -->
            <svg
              class="theme-icon svg-inline--fa fa-sunglasses fa-w-18 fa-7x"
              id="solarIcon"
              aria-hidden="true"
              focusable="false"
              data-prefix="fad"
              data-icon="sunglasses"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 576 512"
            >
              <g class="fa-group">
                <path
                  fill="currentColor"
                  d="M574.09 280.38L528.75 98.66a87.94 87.94 0 0 0-113.19-62.14l-15.25 5.08a16 16 0 0 0-10.12 20.25L395.25 77a16 16 0 0 0 20.22 10.13l13.19-4.39c10.87-3.63 23-3.57 33.15 1.73a39.59 39.59 0 0 1 20.38 25.81l38.47 153.83a276.7 276.7 0 0 0-81.22-12.47c-34.75 0-74 7-114.85 26.75h-73.18c-40.85-19.75-80.07-26.75-114.85-26.75a276.75 276.75 0 0 0-81.22 12.45l38.47-153.8a39.61 39.61 0 0 1 20.38-25.82c10.15-5.29 22.28-5.34 33.15-1.73l13.16 4.39A16 16 0 0 0 180.75 77l5.06-15.19a16 16 0 0 0-10.12-20.21l-15.25-5.08A87.95 87.95 0 0 0 47.25 98.65L1.91 280.38A75.35 75.35 0 0 0 0 295.86v70.25C0 429 51.59 480 115.19 480h37.12c60.28 0 110.38-45.94 114.88-105.37l2.93-38.63h35.76l2.93 38.63c4.5 59.43 54.6 105.37 114.88 105.37h37.12C524.41 480 576 429 576 366.13v-70.25a62.67 62.67 0 0 0-1.91-15.5zM203.38 369.8c-2 25.9-24.41 46.2-51.07 46.2h-37.12C87 416 64 393.63 64 366.11v-37.55a217.35 217.35 0 0 1 72.59-12.9 196.51 196.51 0 0 1 69.91 12.9zM512 366.13c0 27.5-23 49.87-51.19 49.87h-37.12c-26.69 0-49.1-20.3-51.07-46.2l-3.12-41.24a196.55 196.55 0 0 1 69.94-12.9A217.41 217.41 0 0 1 512 328.58z"
                  class="fa-secondary"
                ></path>
                <path
                  fill="currentColor"
                  d="M64.19 367.9c0-.61-.19-1.18-.19-1.8 0 27.53 23 49.9 51.19 49.9h37.12c26.66 0 49.1-20.3 51.07-46.2l3.12-41.24c-14-5.29-28.31-8.38-42.78-10.42zm404-50l-95.83 47.91.3 4c2 25.9 24.38 46.2 51.07 46.2h37.12C489 416 512 393.63 512 366.13v-37.55a227.76 227.76 0 0 0-43.85-10.66z"
                  class="fa-primary"
                ></path>
              </g>
            </svg>
            <!-- 주간 모드 -->
            <svg
              class="theme-icon svg-inline--fa fa-sun fa-w-16 fa-7x"
              id="lightIcon"
              aria-hidden="true"
              focusable="false"
              data-prefix="fad"
              data-icon="sun"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 512 512"
            >
              <g class="fa-group">
                <path
                  fill="currentColor"
                  d="M502.42 240.5l-94.7-47.3 33.5-100.4c4.5-13.6-8.4-26.5-21.9-21.9l-100.4 33.5-47.41-94.8a17.31 17.31 0 0 0-31 0l-47.3 94.7L92.7 70.8c-13.6-4.5-26.5 8.4-21.9 21.9l33.5 100.4-94.7 47.4a17.31 17.31 0 0 0 0 31l94.7 47.3-33.5 100.5c-4.5 13.6 8.4 26.5 21.9 21.9l100.41-33.5 47.3 94.7a17.31 17.31 0 0 0 31 0l47.31-94.7 100.4 33.5c13.6 4.5 26.5-8.4 21.9-21.9l-33.5-100.4 94.7-47.3a17.33 17.33 0 0 0 .2-31.1zm-155.9 106c-49.91 49.9-131.11 49.9-181 0a128.13 128.13 0 0 1 0-181c49.9-49.9 131.1-49.9 181 0a128.13 128.13 0 0 1 0 181z"
                  class="fa-secondary"
                ></path>
                <path
                  fill="currentColor"
                  d="M352 256a96 96 0 1 1-96-96 96.15 96.15 0 0 1 96 96z"
                  class="fa-primary"
                ></path>
              </g>
            </svg>
            <!-- 야간모드 -->
            <svg
              class="theme-icon svg-inline--fa fa-moon-stars fa-w-16 fa-7x"
              id="darkIcon"
              aria-hidden="true"
              focusable="false"
              data-prefix="fad"
              data-icon="moon-stars"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 512 512"
            >
              <g class="fa-group">
                <path
                  fill="currentColor"
                  d="M320 32L304 0l-16 32-32 16 32 16 16 32 16-32 32-16zm138.7 149.3L432 128l-26.7 53.3L352 208l53.3 26.7L432 288l26.7-53.3L512 208z"
                  class="fa-secondary"
                ></path>
                <path
                  fill="currentColor"
                  d="M332.2 426.4c8.1-1.6 13.9 8 8.6 14.5a191.18 191.18 0 0 1-149 71.1C85.8 512 0 426 0 320c0-120 108.7-210.6 227-188.8 8.2 1.6 10.1 12.6 2.8 16.7a150.3 150.3 0 0 0-76.1 130.8c0 94 85.4 165.4 178.5 147.7z"
                  class="fa-primary"
                ></path>
              </g>
            </svg>
            
            <!-- <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;">Themify</span> -->
            <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;"></span>
          </a>
        </li>
      </ul>
    </nav>    
  </div>
</template>

<script>

import axios from "axios";
import constants from '../lib/constants'
import Swal from 'sweetalert2';

export default {
  data() {
    return {
      collapseflag: false,
      isLoggedIn : false,
    }
  },
  created(){
    this.user_check()
  },
  updated(){
    this.user_check()
  },
  props: {
    isHeader: Boolean,
  },
  methods: {
    user_check(){
      if (this.$cookies.isKey('auth-token')){
        this.isLoggedIn = true
      }
      else{
        this.isLoggedIn = false
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
        setTimeout(() => {
          this.$router.push('/').catch(()=>{this.$router.go()})
        },1200)
        const Toast = Swal.mixin({
          toast: true,
          position: 'top-end',
          showConfirmButton: false,
          timer: 1000,
          timerProgressBar: true,
        })

        Toast.fire({
          icon: 'success',
          title: '로그아웃 되었습니다.'
        })
      })
      .catch((error)=>{
        console.log(error.response.data)
      })
    },
    goMain() {
      this.$router.push('/').catch(() => {
        this.$router.go()
      })
    },
    goPerfume() {
      this.$router.push('/perfume').catch(() => {
        this.$router.go()
      })
    },
    goRecommend() {
      if (this.$cookies.isKey('auth-token')){
        this.$router.push('/recommendperfume').catch(() => {
          this.$router.go()
        })
      } else {
        setTimeout(() => {
          this.$router.push('/').catch(()=>{this.$router.go()})
        },1200)
        const Toast = Swal.mixin({
          toast: true,
          position: 'top-end',
          showConfirmButton: false,
          timer: 1000,
          timerProgressBar: true,
        })

        Toast.fire({
          icon: 'error',
          title: '로그인을 하면 향수 추천을 받을 수 있습니다.'
        })
      }
    },
    goProfile() {
      this.$router.push('/user/profile').catch(() => {
        this.$router.go()
      })
    },
  }
}



</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Kufam:wght@800&display=swap');

:root {
  /* font-size: 16px; */
  /* font-family: 'Black Han Sans', sans-serif; */
  --text-primary: #b6b6b6;
  --text-secondary: #ececec;
  --bg-primary: #23232e;
  --bg-secondary: #141418;
  --transition-speed: 600ms;
}

.body {
  color: black;
  background-color: white;
  margin: 0;
  padding: 0;
}

.body::-webkit-scrollbar {
  width: 0.25rem;
}

.body::-webkit-scrollbar-track {
  background: #1e1e24;
  /* background: black; */
}

.body::-webkit-scrollbar-thumb {
  background: #e63c12;
}

/* main {
  margin-left: 5rem;
  padding: 1rem;
} */

.navbar {
  position: fixed;
  background-color: var(--bg-primary);
  transition: width 600ms ease;
  overflow: scroll;
  padding: 0;
}

.navbar-nav {
  /* list-style: none; */
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
}

.nav-item {
  width: 100%;
}

.nav-item:last-child {
  margin-top: auto;
}

.nav-link {
  display: flex;
  align-items: center;
  height: 5rem;
  color: var(--text-primary);
  text-decoration: none;
  filter: grayscale(100%) opacity(0.7);
  transition: var(--transition-speed);
}

.nav-link:hover {
  filter: grayscale(0%) opacity(1);
  /* background: var(--bg-secondary); */
  background: lightgray;
  color: var(--text-secondary);
}

.link-text {
  display: none;
  margin-left: 1rem;
  color:black
}

.nav-link svg {
  width: 1rem;
  min-width: 2rem;
  margin: 0 1.5rem;
}

.fa-primary {
  color: #fa07d9;
}

.fa-secondary {
  color: #f53b1a;
}

.fa-primary,
.fa-secondary {
  transition: var(--transition-speed);
}

.logo {
  font-weight: bold;
  text-transform: uppercase;
  margin-bottom: 0rem;
  text-align: center;
  color: var(--text-secondary);
  background: var(--bg-secondary);
  font-size: 1.5rem;
  letter-spacing: 0.3ch;
  width: 100%;
}

.logo svg {
  transform: rotate(0deg);
  transition: var(--transition-speed);
}

.logo-text
{
  display: inline;
  position: absolute;
  left: -999px;
  transition: var(--transition-speed);
}

.navbar:hover .logo svg {
  transform: rotate(-180deg);
}

/* Small screens */
@media only screen and (max-width: 600px) {
  .navbar {
    bottom: 0;
    width: 100vw;
    height: 5rem;
  }

  .logo {
    display: none;
  }

  .navbar-nav {
    flex-direction: row;
  }

  .nav-link {
    justify-content: center;
  }

  /* main {
    margin: 0;
  } */
}

/* Large screens */
@media only screen and (min-width: 600px) {
  .navbar {
    top: 0;
    width: 5rem;
    height: 100vh;
  }

  .navbar:hover {
    width: 16rem;
  }

  .navbar:hover .link-text {
    display: inline;
  }

  .navbar:hover .logo svg
  {
    margin-left: 11rem;
  }

  .navbar:hover .logo-text
  {
    left: 0px;
  }
}

.dark {
  --text-primary: #b6b6b6;
  --text-secondary: #ececec;
  --bg-primary: #23232e;
  --bg-secondary: #141418;
}

.light {
  --text-primary: #1f1f1f;
  --text-secondary: #000000;
  --bg-primary: #ffffff;
  --bg-secondary: #e4e4e4;
}

.solar {
  --text-primary: #576e75;
  --text-secondary: #35535c;
  --bg-primary: #fdf6e3;
  --bg-secondary: #f5e5b8;
}

.theme-icon {
  display: none;
}

.dark #darkIcon {
  display: block;
}

.light #lightIcon {
  display: block;
}

.solar #solarIcon {
  display: block;
}
</style>