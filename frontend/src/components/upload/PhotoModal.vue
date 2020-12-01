<template>
  <div>
      <div class="modal fade" id="upload" tabindex="-1" aria-labelledby="exampleModalLabel" role="dialog" aria-hidden="true" data-backdrop="static" data-keyboard='false'>
        <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content" style="width:80%; border:0;">
                <div class="modal-header py-1 mb-2" style="background-color:#EFFFE8">
                    <h4 class="modal-title my-auto ml-2" id="exampleModalLabel" style="font-weight:bold;">Triple S</h4>
                    <button type="button" @click='closeModal' class="close my-auto" data-dismiss="modal" aria-label="Close">                    
                    <!-- close -->
                    <span class='mx-2' style='font-size:2rem;' aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div style="background-color:white;">
                
                <div v-if='!loading' class="container" >
                    <form v-if='!uploaded' @submit='uploadImage'>          
                        <div class="container p-0">
                            <div class="row">
                                <div class="form-group col-8">
                                    <label for="recipient-name" class="col-form-label" style='font-weight:bold; font-size:1.5rem;'>Style</label>                            
                                    <br>                                                        
                                    <div class="custom-file ml-2" style='width:100%'>
                                        <input type="file"                                                
                                            id="cloth-image"
                                            class="custom-file-input"
                                            accept=".png, .jpg"  @change='fileSelect' ref='imageCloth' required/>    
                                            <label class="custom-file-label" for="imageCloth" data-browse="사진 찾기">
                                                <p class='mt-1' style='font-size:0.7rem;'>
                                                    {{imageName}}
                                                </p>
                                            </label>                                      
                                    </div>                            
                                </div>
                                <div class='col-1 px-0'></div>
                                <div class="form-group col-2 mb-1 ml-2 px-0" style='text-align:right'>                                    
                                    <div class="custom-control custom-checkbox mt-5">
                                        <input v-model="spo" type="checkbox" class="custom-control-input" id="customCheck1">
                                        <label class="custom-control-label" for="customCheck1" style='font-weight:bold'>공개 여부</label>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="form-group">                                
                            <label for="message-text" class="col-form-label" style='font-weight:bold; font-size:1.5rem;'>Story</label>
                            <textarea v-model="diary" class="form-control ml-2" id="message-text" style='width:95%' rows='4' placeholder="당신의 이야기를 적어주세요."></textarea>
                        </div>                                                

                        <div      
                            @click='uploadImage'                       
                            class="mt-2 row"
                            style="cursor: pointer; margin-left:18%; margin-right:18%;"
                        >
                            <div
                                class="col-12 d-flex justify-content-center align-items-center"
                                style="border:2px solid #2EC4B6; height:2rem; border-radius:5px"
                            >
                            <i class="fas fa-sign-in-alt"></i><span class="ml-2" style="font-weight:bold;">어울리는 향수 찾기</span>
                            </div>
                        </div>                                                                
                    </form>  

                    <div v-if='uploaded'>      
                        <div class='container mt-4'>
                            <div class="row">
                                <div class="col-md-4 col-12 p-0 ml-3" style='height:250px'>
                                    <img :src="server_url+cloth.image" alt="업로드한 옷" style='height:100%'>
                                </div>
                                <div class="col-md-1 col-0 p-0"></div>
                                <div class="col-md-6 col-12 p-0" style='height:250px'>          
                                    <div class='mt-2' style='font-weight: bold; font-size:1rem;'>                                        
                                        <span class='mr-2'>
                                            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-clock" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                                <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm8-7A8 8 0 1 1 0 8a8 8 0 0 1 16 0z"/>
                                                <path fill-rule="evenodd" d="M7.5 3a.5.5 0 0 1 .5.5v5.21l3.248 1.856a.5.5 0 0 1-.496.868l-3.5-2A.5.5 0 0 1 7 9V3.5a.5.5 0 0 1 .5-.5z"/>
                                            </svg>
                                        </span>
                                        {{clothCreated}}                                                                                
                                    </div>
                                    <div class='my-1'>
                                        <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-bar-chart-line mr-2" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                            <path fill-rule="evenodd" d="M11 2a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12h.5a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1H1v-3a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3h1V7a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7h1V2zm1 12h2V2h-2v12zm-3 0V7H7v7h2zm-5 0v-3H2v3h2z"/>
                                        </svg>
                                        <span class="badge badge-info mr-2 px-2 py-1" v-for="adjective in cloth.adjectiveList" :key="adjective">
                                            {{adjective}}
                                        </span>                                        
                                    </div>                                    
                                    <div class='my-1'>
                                        <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-patch-check mr-2" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                            <path fill-rule="evenodd" d="M10.273 2.513l-.921-.944.715-.698.622.637.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01.622-.636a2.89 2.89 0 0 1 4.134 0l-.715.698a1.89 1.89 0 0 0-2.704 0l-.92.944-1.32-.016a1.89 1.89 0 0 0-1.911 1.912l.016 1.318-.944.921a1.89 1.89 0 0 0 0 2.704l.944.92-.016 1.32a1.89 1.89 0 0 0 1.912 1.911l1.318-.016.921.944a1.89 1.89 0 0 0 2.704 0l.92-.944 1.32.016a1.89 1.89 0 0 0 1.911-1.912l-.016-1.318.944-.921a1.89 1.89 0 0 0 0-2.704l-.944-.92.016-1.32a1.89 1.89 0 0 0-1.912-1.911l-1.318.016z"/>
                                            <path fill-rule="evenodd" d="M10.354 6.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7 8.793l2.646-2.647a.5.5 0 0 1 .708 0z"/>
                                        </svg>
                                        <span class="badge badge-success mr-2 px-2 py-1" v-for="line in cloth.lineList" :key="line">
                                            {{line}}
                                        </span>
                                    </div>                       
                                    <div class='my-1'>
                                        <span class='mr-2' v-if='cloth.spo'>
                                            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-unlock" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                                <path fill-rule="evenodd" d="M9.655 8H2.333c-.264 0-.398.068-.471.121a.73.73 0 0 0-.224.296 1.626 1.626 0 0 0-.138.59V14c0 .342.076.531.14.635.064.106.151.18.256.237a1.122 1.122 0 0 0 .436.127l.013.001h7.322c.264 0 .398-.068.471-.121a.73.73 0 0 0 .224-.296 1.627 1.627 0 0 0 .138-.59V9c0-.342-.076-.531-.14-.635a.658.658 0 0 0-.255-.237A1.122 1.122 0 0 0 9.655 8zm.012-1H2.333C.5 7 .5 9 .5 9v5c0 2 1.833 2 1.833 2h7.334c1.833 0 1.833-2 1.833-2V9c0-2-1.833-2-1.833-2zM8.5 4a3.5 3.5 0 1 1 7 0v3h-1V4a2.5 2.5 0 0 0-5 0v3h-1V4z"/>
                                            </svg>
                                            <span class="badge badge-light px-2 py-1 ml-2">
                                                공개
                                            </span>
                                        </span>                                       
                                        <span class='mr-2' v-else>
                                            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-lock" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                                <path fill-rule="evenodd" d="M11.5 8h-7a1 1 0 0 0-1 1v5a1 1 0 0 0 1 1h7a1 1 0 0 0 1-1V9a1 1 0 0 0-1-1zm-7-1a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h7a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-7zm0-3a3.5 3.5 0 1 1 7 0v3h-1V4a2.5 2.5 0 0 0-5 0v3h-1V4z"/>
                                            </svg>   
                                            <span class="badge badge-light px-2 py-1 ml-2">
                                                비공개
                                            </span>
                                        </span>           
                                    </div>                             
                                    <!-- <div v-if='cloth.diary'> -->
                                        
                                        <h4 class='mt-2 mb-1'>Story</h4>
                                        <div class='overflow-auto border border-dark text-break' style='height:100px; font-size:0.8rem; font-weight:bold'>
                                            <div v-if='cloth.diary' class='m-1'>
                                                {{cloth.diary}}
                                            </div>            
                                            <div v-else class='m-1'>
                                                등록된 이야기가 없습니다.
                                            </div>
                                        </div>
                                    <!-- </div>                -->
                                    
                                    <!-- <h6>추천 계열 : {{cloth.}}</h6> -->

                                </div>
                            </div>
                        </div>                        
                        <div class="container mt-4">
                            <div class="row mt-5">
                                <div class='col p-0 m-2' @click='goDetail(perfume.id)' v-for='perfume in perfumes' :key='perfume.id' style="cursor:pointer;">  
                                    <div class="text-center border border-dark" style='height:200px'>
                                        <div class='mt-2 p-0' style='height:130px'>
                                            <img :src='perfume.image' alt="향수 이미지" style='height:100%;'>
                                        </div>
                                        <div class='p-0' style='height:30px'>
                                            <p class='mt-1 mb-0' style='font-size: x-small;'>
                                            {{perfume.brand}} 
                                            <span>
                                                ({{perfume.year}})
                                            </span>
                                            </p>
                                            <p class='mt-0 mb-1' style='font-size: smaller;'>
                                            {{perfume.name}}
                                            </p>
                                        </div>
                                    </div>                                    
                                </div>

                            </div>

                        </div>
                    </div>
                </div>
                <div v-if='loading' class="d-flex justify-content-center">
                    <div class="spinner-border text-success" role="status">
                        <span class="sr-only">Loading...</span>
                    </div>
                </div>                
                <div style="margin-left:10%; margin-right:10%">
                    <hr />
                </div>                
                <!-- <div                 
                    @click='goProfile'   
                    class="mt-2 row"
                    style="cursor: pointer; margin-left:18%; margin-right:18%;"
                >
                    <div
                        class="col-12 d-flex justify-content-center align-items-center"
                        style="border:2px solid #2EC4B6; height:2rem; border-radius:5px"
                    >
                        <i class="far fa-user mr-1"></i><span class="ml-2" style="font-weight:bold">프로필 페이지</span>
                    </div>
                </div>                                               
                <div class="mt-2" style="margin-left:10%; margin-right:10%;">
                    <hr />
                </div> -->

                </div>
                <div class="modal-footer border-0" style="background-color:white;"></div>
            </div>
        </div>
    </div>



      
  </div>
</template>

<script>

import axios from "axios";
import constants from '../../lib/constants'


export default {    
    data() {
        return {            
            loading:false,
            // upload 전
            imageCloth : null,
            imageName:'사진을 선택해주세요 ( jpg, png )',
            spo:false,
            diary:'',
            
            // upload 후
            cloth:null,
            clothCreated:null,
            perfumes:null,
            uploaded:false,
            server_url:constants.SERVER_URL,            
        }
    },
    methods: {
    fileSelect() {
      this.imageCloth = this.$refs.imageCloth.files[0];
      this.imageName = this.$refs.imageCloth.files[0]['name']      
    },    
    uploadImage (e) {
      e.preventDefault();      
      if (this.imageCloth === null) {
          alert('사진을 선택해주세요.')
      } else {
          let formdata = new FormData();
          formdata.append("image", this.imageCloth);
          formdata.append('diary', this.diary)
          formdata.append('spo', this.spo)
            
          let url = `${this.server_url}/api/accounts/clothes/`;      
                
          let token = this.$cookies.get('auth-token')
          let config = {
              headers: {          
                  "Content-Type": "multipart/form-data",          
              Authorization: `Jwt ${token}`,
            }
          }
    
          this.loading = true;
          axios
            .post(url, formdata, config)
            .then((res) => {                          
                this.cloth = res.data.data            
                this.clothCreated = res.data.data.created_at.substring(0,10) + ' ' + res.data.data.created_at.substring(11,16)
                this.perfumes = res.data.perfumedata      
                this.uploaded = !this.uploaded                               
                this.loading= false;
            })
            .catch((err) => {
              console.log(err);
            });
      }
    },   
    closeModal() {
        this.uploaded=false
        this.imageCloth = null
        this.imageName='사진을 선택해주세요 ( jpg, png )'
        this.spo=false
        this.diary=''
    },
    goProfile() {
        // this.closeModal()
        this.$router.push('/user/profile').then(()=> {this.$router.go()}).catch(() => {            
            this.$router.go()
      })
    },
    goDetail(id) {
        // this.closeModal()
        this.$router.push(`/perfumedetail/${id}`).then(()=> {this.$router.go()}).catch(() => {
            this.$router.go()          
        })
    },

    },

    mounted() {
        
    },
}
</script>

<style>

</style>