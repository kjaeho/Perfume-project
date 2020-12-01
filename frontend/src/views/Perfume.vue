<template>
  <div class="container col-md-10" style="margin-left:10%;">
    <!-- 최신순 브랜드 계열 성별 -->
    <div class="d-flex row mt-4 mb-2">
      <b-button @click="resetPerfumeData" size="lg" class="latestbtn my-auto col-12 col-sm-6 col-md-3 col-lg-3" style="border:1px solid crimson;">Latest</b-button>
      <b-dropdown variant="outline-danger" size="lg" text="Brand" class="col-12 col-sm-6 col-md-3 col-lg-3 my-auto p-0" style="width:23%">
        <b-dropdown-item-button @click="selectBrand('Acqua di Parma')"><span style="font-weight:bold;">Acqua di Parma</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Bulgari')"><span style="font-weight:bold;">Bulgari</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Burberry')"><span style="font-weight:bold;">Burberry</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Byredo')"><span style="font-weight:bold;">Byredo</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Calvin Klein')"><span style="font-weight:bold;">Calvin Klein</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Cartier')"><span style="font-weight:bold;">Cartier</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Chanel')"><span style="font-weight:bold;">Chanel</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Christian Dior')"><span style="font-weight:bold;">Christian Dior</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Creed')"><span style="font-weight:bold;">Creed</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Demeter Fragrance Library')"><span style="font-weight:bold;">Demeter Fragrance Library</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Diptyque')"><span style="font-weight:bold;">Diptyque</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Dolce & Gabbana')"><span style="font-weight:bold;">Dolce & Gabbana</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Editions de Parfums Frederic Malle')"><span style="font-weight:bold;">Editions de Parfums Frederic Malle</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Estée Lauder')"><span style="font-weight:bold;">Estée Lauder</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Giorgio Armani')"><span style="font-weight:bold;">Giorgio Armani</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Givenchy')"><span style="font-weight:bold;">Givenchy</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Gucci')"><span style="font-weight:bold;">Gucci</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Hermès')"><span style="font-weight:bold;">Hermès</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Hugo Boss')"><span style="font-weight:bold;">Hugo Boss</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Jo Malone London')"><span style="font-weight:bold;">Jo Malone London</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Kenzo')"><span style="font-weight:bold;">Kenzo</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Lacoste')"><span style="font-weight:bold;">Lacoste</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Le Labo')"><span style="font-weight:bold;">Le Labo</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('L\'Occitane')"><span style="font-weight:bold;">L'Occitane</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Maison Francis Kurkdjian')"><span style="font-weight:bold;">Maison Francis Kurkdjian</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Montana')"><span style="font-weight:bold;">Montana</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Penhaligon\'s')"><span style="font-weight:bold;">Penhaligon's</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Prada')"><span style="font-weight:bold;">Prada</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Santa Maria Novella')"><span style="font-weight:bold;">Santa Maria Novella</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Serge Lutens')"><span style="font-weight:bold;">Serge Lutens</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Tom Ford')"><span style="font-weight:bold;">Tom Ford</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectBrand('Yves Saint Laurent')"><span style="font-weight:bold;">Yves Saint Laurent</span></b-dropdown-item-button>
        <b-dropdown-item-button>========================</b-dropdown-item-button>
      </b-dropdown>
      <b-dropdown variant="outline-danger" size="lg" text="Perfume Line" class="col-12 col-sm-6 col-md-3 col-lg-3 my-auto p-0" style="">
        <b-dropdown-item-button @click="selectLine('FLORAL')"><span style="font-weight:bold;">FLORAL</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectLine('CITRUS')"><span style="font-weight:bold;">CITRUS</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectLine('CHYPRE')"><span style="font-weight:bold;">CHYPRE</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectLine('ORIENTAL')"><span style="font-weight:bold;">ORIENTAL</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectLine('FRUITY')"><span style="font-weight:bold;">FRUITY</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectLine('WOODY')"><span style="font-weight:bold;">WOODY</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectLine('GREEN')"><span style="font-weight:bold;">GREEN</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectLine('SPICY')"><span style="font-weight:bold;">SPICY</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectLine('ALDEHYDE')"><span style="font-weight:bold;">ALDEHYDE</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectLine('FOUGERE')"><span style="font-weight:bold;">FOUGERE</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectLine('GOURMAND')"><span style="font-weight:bold;">GOURMAND</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectLine('MUSK')"><span style="font-weight:bold;">MUSK</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectLine('VANILLA')"><span style="font-weight:bold;">VANILLA</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectLine('LEATHER')"><span style="font-weight:bold;">LEATHER</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectLine('AROMATIC')"><span style="font-weight:bold;">AROMATIC</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectLine('AQUATIC')"><span style="font-weight:bold;">AQUATIC</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectLine('COTTON')"><span style="font-weight:bold;">COTTON</span></b-dropdown-item-button>
        <b-dropdown-item-button>========================</b-dropdown-item-button>
      </b-dropdown>
      <b-dropdown variant="outline-danger" size="lg" text="Gender" class="col-12 col-sm-6 col-md-3 col-lg-3 my-auto p-0" style="">
        <b-dropdown-item-button @click="selectGender('FOR MEN')"><span style="font-weight:bold;">FOR MEN</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectGender('FOR WOMEN')"><span style="font-weight:bold;">FOR WOMEN</span></b-dropdown-item-button>
        <b-dropdown-item-button @click="selectGender('FOR UNISEX')"><span style="font-weight:bold;">FOR UNISEX</span></b-dropdown-item-button>
        <b-dropdown-item-button>========================</b-dropdown-item-button>
      </b-dropdown>
    </div>

    <!-- 선택한 장르 나타내기 -->
    <div v-if="choiceBrand || choiceGender || choiceLine" class="p-3">
      <i class="fas fa-search-plus" style="color:black; font-size:1.4rem"><span class="ml-2">Category 검색 결과 :</span></i>
      <span v-if="choiceLine" style="color:black; font-size:1.4rem; font-weight:bold" class="ml-2">{{choiceLine}}</span>
      <span v-if="choiceBrand" style="color:black; font-size:1.4rem; font-weight:bold" class="ml-2">{{choiceBrand}}</span>
      <span v-if="choiceGender" style="color:black; font-size:1.4rem; font-weight:bold" class="ml-2">{{choiceGender}}</span>
    </div>

    <div v-if="perfumeData">
      <div class="card text-white col-12 col-sm-6 col-md-4 col-lg-3 p-4" style="border:none; display:inline-block;" v-for="perfume in perfumeData" :key="perfume.id">
        
        <div @click="goDetail(perfume.id)" class="property-card" style="cursor:pointer;">
            <div class="property-image" :style="{ backgroundImage: 'url(' + perfume.image + ')' }">
              <!-- <img :src="perfume.image" class="property-image" alt=""> -->
              <div class="property-image-title">
                <!-- Optional <h5>Card Title</h5> If you want it, turn on the CSS also. -->
              </div>
            </div>
          <div class="property-description">
            <!-- 민규야 좀 이쁘게 꾸며놔라 -->
            <small class="mr-2" style="color:whitesmoke; font-weight:bold">{{perfume.brand}}</small>
            <!-- 0 여자 1남자 2중성 -->
            <i v-if="perfume.gender==0" class="fas fa-venus" style="color:red"></i> 
            <i v-if="perfume.gender==1" class="fas fa-mars" style="color:blue"></i>
            <i v-if="perfume.gender==2" class="fas fa-venus-mars" style=""></i>
            <h5 class="mt-2" style="font-size:1.2rem">{{perfume.name}}</h5>
            <!-- <small>민규야 이쁘게 꾸며놔</small> -->
            <div class="d-flex justify-content-center my-2">
              <!-- 향수 계열 badge -->
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

    <div v-if="perfumeData.length == 0" class="d-flex justify-content-center" style="margin:10rem">
      <span style="color:white; font-weight:bold; font-size:2rem">검색 결과가 없습니다 :)</span>
    </div>


    <!-- pagination -->
    <div v-if="flag" class="mt-3">
      <b-pagination v-model="currentPage" :total-rows="rows" align="center"></b-pagination>
    </div>

    <div v-if="!flag" class="mt-3">
      <b-pagination v-model="currentPageForSpecific" :total-rows="rows" align="center"></b-pagination>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import constants from '../lib/constants'

export default {
  data() {
    return {
        perfumeData:{},
        rows:'',
        perfumeBrand:0,
        perfumeGender:0,
        perfumeLine:0,
        flag:true,
        currentPage:1,
        currentPageForSpecific:1,
        choiceBrand:'',
        choiceGender:'',
        choiceLine:'',
    }
},
created(){
  this.getData()
},
methods:{
    getData() {
      this.flag=true
      axios.get(constants.SERVER_URL + `/api/perfumes/recent-list/${this.currentPage}/`)
        .then((res) => {
            this.perfumeData = res.data.perfumeData
            this.rows=res.data.pageNum
        })
        .catch((err)=>{
            console.log(err)
        })
    },
    getSpecificData(){
      const gender=this.perfumeGender
      const brand=this.perfumeBrand
      const line=this.perfumeLine
      this.currentPage=1
      this.flag=false
      axios.get(constants.SERVER_URL+`/api/perfumes/listby-category/${gender}/${brand}/${line}/${this.currentPageForSpecific}/`)
        .then((res)=>{
          this.perfumeData=res.data.perfumeData
          this.rows=res.data.pageNum
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    resetPerfumeData(){
      this.perfumeGender=0
      this.perfumeBrand=0
      this.perfumeLine=0
      this.choiceGender = ""
      this.choiceBrand = ""
      this.choiceLine = ""
      this.getData()
    },
    goDetail(id) {
        this.$router.push(`/perfumedetail/${id}`)
        .catch(() => {
            this.$router.go()          
        })
    },
    selectBrand(brand) {
      this.perfumeBrand = brand
      this.choiceBrand = brand
      this.getSpecificData()
    },
    selectGender(gender) {
      if (gender == 'FOR MEN') {
        this.perfumeGender = 1
      } else if (gender == 'FOR WOMEN') {
        this.perfumeGender = 0
      } else if (gender =='FOR UNISEX') {
        this.perfumeGender = 2
      }
      this.choiceGender = gender
      this.getSpecificData()
    },
    selectLine(line) {
      this.perfumeLine = line
      this.choiceLine = line
      this.getSpecificData()
    },
    resetsPage(){
      if (this.currentPageForSpecific>=2){
        this.currentPageForSpecific=1
      }
    },
  },
  watch:{
    currentPage(){
      this.getData()
    },
    currentPageForSpecific(){
      this.getSpecificData()
    },
    movieGenre(){
      this.resetsPage()
    },
    movieNation(){
      this.resetsPage()
    },
    movieYear(){
      this.resetsPage()
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