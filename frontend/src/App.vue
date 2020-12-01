<template>
  <div id="app">
    <Header :isHeader="isHeader" />
    <router-view/>
    <LoginModal />
    <JoinModal />
    <PhotoModal />
    <!-- <PhotoDetailModal /> -->
    <!-- <Main @childs-event="goapp(data)"/> -->
  </div>
</template>

<script> 
import Header from '@/components/Header'
import constants from '@/lib/constants'
import LoginModal from '../src/components/login/LoginModal.vue'
import JoinModal from '../src/components/join/JoinModal.vue'
import PhotoModal from '../src/components/upload/PhotoModal.vue'
// import PhotoDetailModal from '../src/components/main/PhotoDetailModal.vue'
// import Main from '../src/views/Main.vue'
export default {
  name: 'App',
  components: { 
    Header,
    LoginModal,
    JoinModal,
    PhotoModal,
    // PhotoDetailModal,
    // Main
  },
  
  

  
  created() {
      let url = this.$route.name;
  
      this.checkUrl(url);

      console.log('App.vue')
    let token = window.$cookies.get('FootballDiary')
    if (token) {
      this.$store.commit('setToken', token)
      console.log('App.vue.afterSetToken')
      this.$store.dispatch('getUserFromServer')
    } else {
      // this.onLogout()
  }
  },
  watch: {
      $route (to){
          this.checkUrl(to.name);
      }
  },
  methods : {
      checkUrl(url) { 

          let array = [
              constants.URL_TYPE.USER.LOGIN,
              constants.URL_TYPE.USER.JOIN,
          ];

          let isHeader = true;
          array.map(path => {
              if (url === path)
                  isHeader = false;
          })
          this.isHeader = isHeader;

      },
      goapp(data) {
        this.photoData = data
        console.log("dmdk",data)
      }
      
  },
  data: function () {
        return {
            isHeader: true,
            constants,
            photoData:[],
        } 
    }
}
</script>

<style>
.app {
  /* background-color: rgb(53, 52, 52); */
}
</style>
