<template>
  <div>
    <div class="container col-md-10 mt-5" style="margin-left:10%;" v-if="searchPerfume">

        <div>
          <span class="my-auto ml-3" style="color:pink; font-size:3rem; font-weight:bold;">{{this.$cookies.get('searchKeyword')}}</span>
          <span class="ml-2" style="font-size:1.5rem; font-weight:bold; ">과(와) 관련된 향수 검색 결과 :)</span>
        </div>
        <div class="card mt-5 text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4" style="border:none; display:inline-block;" v-for="perfume in searchPerfume" :key="perfume.id">
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
    <div class="mt-3">
        <b-pagination v-model="currentPage" :total-rows="rows" align="center"></b-pagination>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import constants from '../lib/constants';

export default {
    data() {
        return {
            searchPerfume: [],
            currentPage:1,
            rows:'',
        }
    },
    methods: {
        getSearch() {
            let searchKeyword = this.$cookies.get('searchKeyword')
            axios.get(`${constants.SERVER_URL}/api/perfumes/search/${searchKeyword}/${this.currentPage}`)
            .then((res) => {
                this.searchPerfume = res.data.perfumeData
                this.rows=res.data.pageNum
            })
        },
        goDetail(id) {
            this.$router.push(`/perfumedetail/${id}`).catch(() => {
                this.$router.go()          
            })
        },

    },
    created(){
        this.getSearch()
    },
    watch:{
        currentPage(){
            this.getSearch()
        },
    }
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