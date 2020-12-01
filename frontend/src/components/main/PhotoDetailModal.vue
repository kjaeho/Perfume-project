<template>
  <div>
      
      <div class="modal fade" id="photodetail" role="dailog" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
            <div class="modal-header" style="background-color:#EFFFE8">
                <h5 class="modal-title" id="exampleModalLabel">Triple S.  #{{photoData.id}}</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <div class='container mt-4'>
                    <div class="row">
                        <div class="col-md-4 col-12 p-0 ml-3" style='height:250px'>
                            <img :src="server_url+photoData.image" alt="업로드한 옷" style='max-width:100%'>
                            <b-button v-if="photoData.user==username" variant="outline-danger" style='min-width:100%;margin-top:0.5rem;' @click="deleteClothes">삭제</b-button>
                        </div>
                        <div class="col-md-1 col-0 p-0"></div>
                        <div class="col-md-6 col-12 p-0 text-left float-left" style='height:250px'>          
                            <div class='mt-2' style='font-weight: bold; font-size:1rem;'>                                        
                                <span class='mr-2'>
                                    <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-clock" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                        <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm8-7A8 8 0 1 1 0 8a8 8 0 0 1 16 0z"/>
                                        <path fill-rule="evenodd" d="M7.5 3a.5.5 0 0 1 .5.5v5.21l3.248 1.856a.5.5 0 0 1-.496.868l-3.5-2A.5.5 0 0 1 7 9V3.5a.5.5 0 0 1 .5-.5z"/>
                                    </svg>
                                </span>
                                {{photoData.created_at | moment("calendar")}}                                                                                                       
                            </div>
                            <div class='my-1'>
                                <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-bar-chart-line mr-2" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd" d="M11 2a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12h.5a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1H1v-3a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3h1V7a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7h1V2zm1 12h2V2h-2v12zm-3 0V7H7v7h2zm-5 0v-3H2v3h2z"/>
                                </svg>
                                <span class="badge badge-info mr-2 px-2 py-1" v-for="adjective in photoData.adjectiveList" :key="adjective">
                                    {{adjective}}
                                </span>                                        
                            </div>                                    
                            <div class='my-1'>
                                <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-patch-check mr-2" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd" d="M10.273 2.513l-.921-.944.715-.698.622.637.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01.622-.636a2.89 2.89 0 0 1 4.134 0l-.715.698a1.89 1.89 0 0 0-2.704 0l-.92.944-1.32-.016a1.89 1.89 0 0 0-1.911 1.912l.016 1.318-.944.921a1.89 1.89 0 0 0 0 2.704l.944.92-.016 1.32a1.89 1.89 0 0 0 1.912 1.911l1.318-.016.921.944a1.89 1.89 0 0 0 2.704 0l.92-.944 1.32.016a1.89 1.89 0 0 0 1.911-1.912l-.016-1.318.944-.921a1.89 1.89 0 0 0 0-2.704l-.944-.92.016-1.32a1.89 1.89 0 0 0-1.912-1.911l-1.318.016z"/>
                                    <path fill-rule="evenodd" d="M10.354 6.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7 8.793l2.646-2.647a.5.5 0 0 1 .708 0z"/>
                                </svg>
                                <span class="badge badge-success mr-2 px-2 py-1" v-for="line in photoData.lineList" :key="line">
                                    {{line}}
                                </span>
                            </div>                       
                            <div class='my-1'>
                                <span class='mr-2' v-if='photoData.spo'>
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
                                <div class='overflow-auto text-break' style='height:100px; font-size:0.8rem; font-weight:bold'>
                                    <div v-if='photoData.diary' class='m-1'>
                                        {{photoData.diary}}
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
                        <div class='col p-0 m-2' @click='goDetail(perfume.id)' v-for='perfume in photoData.perfumedata' :key='perfume.id' style="cursor:pointer;" data-dismiss="modal">  
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
        </div>
    </div>
  </div>
</template>

<script>
import constants from '../../lib/constants'

export default {
    props:['photoData','username'],
    data() {
        return {
            blank: " ",
            server_url:constants.SERVER_URL,
        }
    },
    methods: {
        goDetail(id) {
            this.$router.push(`/perfumedetail/${id}`)
        .catch(() => {
            this.$router.go(`/`)          
            })
        },
        deleteClothes(){
            this.$emit('deleteClothes',this.photoData.id)
        }
    },
}
</script>

<style>

</style>