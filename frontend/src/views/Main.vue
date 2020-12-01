<template>
    <div>  
        <section :style="carouselStyle">
            <div id="carouselExampleFade" class="carousel slide" data-ride="carousel">
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src="../../src/assets/img/carousel_perfume_1.jpg" class="d-block" style="width:100%;height:47rem;opacity:0.6" alt="...">
                    </div>
                    <div class="carousel-item">
                        <img src="../../src/assets/img/carousel_perfume_2.jpg" class="d-block" style="width:100%;height:47rem;opacity:0.6" alt="...">
                    </div>
                    <div class="carousel-item">
                        <img src="../../src/assets/img/carousel_perfume_3.jpg" class="d-block" style="width:100%;height:47rem;opacity:0.6" alt="...">
                    </div>
                </div>
                <a class="carousel-control-prev" href="#carouselExampleFade" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                </a>
                <a class="carousel-control-next" href="#carouselExampleFade" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                </a>
            </div>
            <div class="d-flex justify-content-center align-items-center" :style="searchbar">
                <div class="form-group d-flex justify-content-center row" style="width:100%">
                    <span class="col-12 d-flex justify-content-center pb-2" :style="mainTitle">Scent . Sense . Style</span>
                    <i class="fas fa-search my-auto mr-2" :style="searchbarIcon"></i>
                    <input @keypress.enter="Search(search)" v-model="search" class="form-control" :style="carouselSearchbar" placeholder="찾고 싶은 향수를 입력해보세요!">
                </div>
            </div>
            <div class="mx-auto text-center float-center" :style="scrolled">
                <h2>
                    <b-icon
                        animation="fade"
                        icon="mouse"
                        variant="dark"
                        class=""
                        style="cursor:pointer;"
                        @click="moveBottom"
                    ></b-icon>
                </h2>
            </div>
        </section>
            
        <br>
        <div id="maintext" :style="display">
            <div class="d-inline-block mb-4" v-for="d in reviewData" :key="d.id" :style="reviewNum">
                <div class="card" style="width:24rem;height:34rem;" data-toggle="modal" data-target="#photodetail" @click="photo(d)">
                    <img :src="server_url + d.image" class="card-img-top" alt="..." style="width:100%;height:65% !important;">
                    <div class="card-body">
                        <p>{{d.created_at  | moment("calendar")}}</p>
                        <p v-if="!d.diary">등록된 Diary가 없습니다.</p>
                        <p v-if="d.diary">{{d.diary}}</p>
                        <p>{{d.tag}}</p>
                    </div>
                </div>
                <PhotoDetailModal
                    :photoData='photoData'
                     />   
            </div>

        
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import constants from '../lib/constants'
import PhotoDetailModal from '../components/main/PhotoDetailModal.vue'

export default {
    components: {
        PhotoDetailModal,
    },
    data() {
        return {
            search: "",
            reviewData:[],
            viewModal:false,
            modalData:Object,
            photoData:{},
            display:"margin-left:10rem",
            nowWidth: Number,
            carouselStyle: "padding-left:4%;",
            carouselSearchbar: "width:25rem; height:3rem; opacity:0.9; border-radius:15px;background-color:light",
            searchbarIcon:"font-size:3rem; color:dark;",
            searchbar:"position:absolute;top:40%; left:20%",
            mainTitle: "color:dark; font-family: 'Black Han Sans', sans-serif; font-size:3rem;left:1rem",
            scrolled : "position:absolute;top:80%; left:50%;",
            server_url:constants.SERVER_URL,
            reviewNum:"width:33%;cursor:pointer;"
        }
    },
    created(){
        this.getReview()
    },
    mounted() {
        window.addEventListener('resize', this.handleResize);
        this.handleResize();
    },
    destroyed() {
        window.removeEventListener('resize',this.handleResize);
    },
    methods:{
        getReview(){
            axios.get(constants.SERVER_URL+'/api/accounts/clothes/main/')
            .then((res)=>{
                this.reviewData = res.data.data.filter(item => item.spo == 1)
            })
            this.nowWidth = window.innerWidth
            if (this.nowWidth < 540) {
                this.display = ""
            }
        },
        Search(data) {
            this.$cookies.set('searchKeyword',data)
            this.$router.push('/searchperfume').catch(() => {
                this.$router.go()
            })
        },
        
        photo(data) {
            this.photoData = data
        },
        handleResize() {
            this.nowWidth = window.innerWidth
            if (this.nowWidth < 540) {
                this.display = ""
                this.carouselStyle = ""
                this.carouselSearchbar = "width:80%;height:3rem; opacity:0.9; border-radius:15px;background-color:light"
                this.searchbarIcon = "font-size:1rem; color:dark;"
                this.searchbar = "position:absolute;top:30%"
                this.mainTitle = "color:dark; font-family: 'Black Han Sans', sans-serif; font-size:1.7rem;"
                this.scrolled = "position:absolute;top:60%; left:50%;"
                this.reviewNum = "width:50%;cursor:pointer;"
            }else{
                this.display = "margin-left:12%"
                this.carouselStyle = "padding-left:4%;"
                this.carouselSearchbar = "width:25rem; height:3rem; opacity:0.9; border-radius:15px;background-color:light"
                this.searchbarIcon = "font-size:3rem; color:dark;"
                this.searchbar = "position:absolute;top:40%; left:20%"
                this.mainTitle = "color:dark; font-family: 'Black Han Sans', sans-serif; font-size:3rem;left:1rem"
                this.scrolled = "position:absolute;top:80%; left:50%;"
                this.reviewNum = "width:33%;cursor:pointer;"
            }
        },
        
        moveBottom() {
            var location = document.querySelector("#maintext").offsetTop;
            window.scrollTo({ top: location - 25, behavior: "smooth" });
        },
        
    },
}
</script>

<style>

</style>