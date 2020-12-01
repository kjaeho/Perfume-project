<template>
  <div class="container">
      <form @submit='uploadImage'>
          <!-- <p>
            <input type="text" placeholder='Title' id='title' value={this.state.title} onChange={this.handleChange} required/>
          </p>           -->
          <p>
            <input type="file"
                   id="cloth-image"
                   accept=".png, .jpg"  @change='fileSelect' ref='imageCloth' required/>
          </p>
          <input type="submit"/>
        </form>  
      <div>
      <img :src="server_url+image" alt="업로드한 옷 뜨게 해줘야지" style='height:10rem;'>
      <p>여기 이제 추천 받은 향수들 보여줄거임</p>
      </div>
  </div>
</template>

<script>

import axios from "axios";

export default {
  data() {
    return {
      server_url : "http://localhost:8000",
      imageCloth : null,
      image:null,

    }

  },
  methods: {
    fileSelect() {
      this.imageCloth = this.$refs.imageCloth.files[0];
    },
    uploadImage (e) {
      e.preventDefault();
      let formdata = new FormData();
      formdata.append("image", this.imageCloth);

      let url = `${this.server_url}/api/accounts/clothes/`;      
      
      // 토큰을 어떻게 가져올지는 고민해봐 localstorage 쓸지 store에 저장할지
      // 일단은 admin 꺼 가져옴
      let token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InRlc3RAdGVzdC5jb20iLCJleHAiOjE2MDQ4MTcyMDQsImVtYWlsIjoidGVzdEB0ZXN0LmNvbSIsIm9yaWdfaWF0IjoxNjA0NzMwODA0fQ.eJsUakSsULyzTtXHAanscF3l0Yv8J5LURP-x-5kEQeA"
      let config = {
        headers: {
          // form 형태로 보내려면 이 짓한다
          "Content-Type": "multipart/form-data",
          // 이건 jwt 토큰으로 보안 걸어서임
          Authorization: `Jwt ${token}`,
        }
      }

      axios
        .post(url, formdata, config)
        .then((res) => {          
          console.log(res);          
          this.image = res.data.data.image
        })
        .catch((err) => {
          console.log(err);
        });
    }

  },

}
</script>

<style>

</style>