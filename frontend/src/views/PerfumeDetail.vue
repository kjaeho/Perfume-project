<template>
  <div class="container col-md-10 d-flex justify-content-center" style="padding-left:10%; padding-right:5%;">
      <div class="d-flex row" style="margin-top:5rem; margin-bottom:5rem; width:100%">
        <div class="col-md-6" style="">
          <img v-if="perfume.image" :src="perfume.image" style="width:25rem; height:25rem;">
        </div>
        <div class="col-md-6 m-0 p-0">
          <!-- 향수 이름 -->
          <span style="font-family: 'Black Han Sans', sans-serif; font-size:1.5rem">PERFUME NAME</span>
          <br>
          <span style="font-family: 'Black Han Sans', sans-serif; color:red; font-size:1.4rem; white-space:pre-line;">{{perfume.name}}</span>
          
          <!-- 브랜드 -->
          <br>
          <br>
          <span style="font-family: 'Black Han Sans', sans-serif; font-size:1.5rem">PERFUME BRAND</span>
          <br>
          <img v-if="perfume.brand == 'Acqua di Parma '" src="../assets/img/acqua_di_parma.jpg" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Bulgari '" src="../assets/img/bulgari.jpg" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Burberry '" src="../assets/img/burberry.jpg" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Byredo '" src="../assets/img/byredo.jpg" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Calvin Klein '" src="../assets/img/calvin-klein.jpg" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Cartier '" src="../assets/img/cartier.png" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Chanel '" src="../assets/img/chanel.jpg" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Christian Dior '" src="../assets/img/dior.png" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Creed '" src="../assets/img/creed.png" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Demeter Fragrance Library '" src="../assets/img/demeter.jpg" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Diptyque '" src="../assets/img/diptyque.png" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Dolce & Gabbana '" src="../assets/img/dolce.jpg" style="width:11rem; height:6rem;">
          <img v-if="perfume.brand == 'Editions de Parfums Frederic Malle '" src="../assets/img/frederic.jpg" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Estée Lauder '" src="../assets/img/estee.png" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Giorgio Armani '" src="../assets/img/giorgio.jpg" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Givenchy '" src="../assets/img/givenchy.png" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Gucci '" src="../assets/img/gucci.jpg" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Hermès '" src="../assets/img/hermes.png" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Hugo Boss '" src="../assets/img/boss.png" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Jo Malone London '" src="../assets/img/jomalone.jpg" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Kenzo '" src="../assets/img/kenzo.png" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Lacoste '" src="../assets/img/lacoste.jpg" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Le Labo '" src="../assets/img/lelabo.jpg" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'L\'Occitane '" src="../assets/img/loccitane.png" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Maison Francis Kurkdjian '" src="../assets/img/masion.jpg" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Montana '" src="../assets/img/montana.png" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Penhaligon\'s '" src="../assets/img/penhaligons.png" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Prada '" src="../assets/img/prada.png" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Santa Maria Novella '" src="../assets/img/santamaria.png" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Serge Lutens '" src="../assets/img/serge.png" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Tom Ford '" src="../assets/img/tomford.png" style="width:10rem; height:6rem;">
          <img v-if="perfume.brand == 'Yves Saint Laurent '" src="../assets/img/saint.png" style="width:10rem; height:6rem;">

          <!-- 성별 -->
          <br>
          <br>
          <span style="font-family: 'Black Han Sans', sans-serif; font-size:1.5rem">GENDER</span>
          <br>
          <img v-if="perfume.gender == 0" src="../assets/img/woman.png" style="width:5rem; height:5rem">
          <span v-if="perfume.gender == 0" class="ml-3" style="font-weight:bold">FOR WOMAN</span>
          <img v-if="perfume.gender == 1" src="../assets/img/man.png" style="width:5rem; height:5rem">
          <span v-if="perfume.gender == 1" class="ml-3" style="font-weight:bold">FOR MAN</span>
          <img v-if="perfume.gender == 2" src="../assets/img/unisex.jpg" style="width:8rem">
          <span v-if="perfume.gender == 2" class="ml-3" style="font-weight:bold">FOR UNISEX</span>
        </div>
        <!-- detail  -->
        <div class="mt-5" style="width:100%">
          <hr>
          <span style="font-family: 'Black Han Sans', sans-serif; font-size:1.5rem">PERFUME RELEASE</span>
          <div style="width:15rem; background-color:red;">
            <small style="visibility :hidden">d</small>
          </div>
          <br>
          <div class="d-flex justify-content-between">
            <span style="font-weight:bold; font-size:1rem">{{perfume.year}}년 출시</span>
            <span class="" style="font-weight:bold; color:red" v-if="perfume.state == 0">DISCONTINUED</span>
            <span class="" style="font-weight:bold; color:blue" v-if="perfume.state == 1">IN PRODUCTION</span>
          </div>
          <br><br>
          <!-- discription -->
          <span style="font-family: 'Black Han Sans', sans-serif; font-size:1.5rem">PERFUME DATA</span>
          <div style="width:15rem; background-color:red;">
            <small style="visibility :hidden">d</small>
          </div>
          <br>
          <p style="font-weight:bold;">{{perfume.info}}</p>
          <br><br>
          <!-- 계열 -->
          <span style="font-family: 'Black Han Sans', sans-serif; font-size:1.5rem">PERFUME LINE</span>
          <div style="width:15rem; background-color:red;">
            <small style="visibility :hidden">d</small>
          </div>
          <br>
          <div v-if="perfume.lineList == false">
            <p style="font-weight:bold; font-size:1.3rem">해당 향수는 계열에 대한 정보가 제공되지 않습니다.</p>
          </div>
          <div v-for="line in perfume.lineList" :key="line.id" style="display:inline-block; width:50%;">
            <div style="">
              <img v-if="line == 'Floral'" src="../assets/img/floral.jpg" style="width:50%; height:12rem;">
              <p v-if="line == 'Floral'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Floral'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">가장 대표적이고 기본적인 향으로, 향 중에 여성뿐만 아니라 남성향수에도 많이 사용됩니다. 사용되는 꽃의 종류에 따라 청초하고 청순하며, 세련되고 화려한 이미지의 변화가 가능합니다. 누구에게나 부담이 없이 익숙한 향입니다.</small>
              </div>

              <img v-if="line == 'Aldehyde'" src="../assets/img/aldehyde.jpg" style="width:50%; height:12rem;">
              <p v-if="line == 'Aldehyde'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Aldehyde'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">향수에서 'Aldehyde'라는 말은 지방족 화합물, 지방이란 뜻으로 Floral, Fruity 계열 등과 함께 할 때 쾌적한 향기를 표현합니다. 자스민(Jasmine), 로즈(Rose), 백합(Lily), 은방울꽃 등에 신선한 바람과 같은 향을 더해줍니다.</small>
              </div>

              <img v-if="line == 'Aromatic'" src="../assets/img/aromatic.jpg" style="width:50%; height:12rem;">
              <p v-if="line == 'Aromatic'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Aromatic'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">아로마 계열의 향수는 향이 강한 허브나 향신료가 중심이 됩니다. 식물 자체에 강한 향이 있는 세이지(sage), 로즈마리(rosemary), 민트(mint), 라벤더(lavender), 갈바늄(Galbanum)등의 허브 종류가 아로마 계열의 향수에 주로 사용됩니다.</small>
              </div>

              <img v-if="line == 'Aquatic'" src="../assets/img/aquatic.jpg" style="width:50%; height:12rem;">
              <p v-if="line == 'Aquatic'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Aquatic'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">파도치는 바다를 연상하게 하는 상쾌하고 시원한 향입니다. 대부분 여름철에 어울리는 향수라고 하지만, 아주 추운 겨울에 머플러 부분에 뿌리면 더욱 강한 향과 매력을 발산할 수 있는 향입니다. 많은 향에서 Citrus계열과 함께 사용됩니다.</small>
              </div>

              <img v-if="line == 'Chypre'" src="../assets/img/chypre.jpg" style="width:50%; height:12rem;">
              <p v-if="line == 'Chypre'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Chypre'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">Chypre는 지중해의 시프러스 섬으로부터 유래되었으며, 나뭇잎이 축축하게 젖은 듯 하면서도 그을은 듯한 향조로 마음을 편안히 가라않게 하는 것이 특징이며, 떡갈나무에 서식하는 떡갈나무이끼를 기초로 하여 베르가못의 액센트가 조화를 이룬 향기를 말합니다.</small>
              </div>

              <img v-if="line == 'Citrus'" src="../assets/img/citrus.jpg" style="width:50%; height:12rem;">
              <p v-if="line == 'Citrus'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Citrus'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">시트러스(Citrus) 향 계열은 헤스페리딘 이라는 성분을 포함한 감귤류의 향조를 일컫는 말로 레몬, 베르가못, 라임, 블러드 오렌지 등과 같은 과일 또는 페티그레인, 네롤리 등의 식물로도 표현됩니다. Fruit 계열의 향과 함께 사용됩니다.</small>
              </div>

              <img v-if="line == 'Cotton'" src="../assets/img/cotton.jpg" style="width:50%; height:12rem;">
              <p v-if="line == 'Cotton'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Cotton'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">방금 씻고 나온 듯한 샤워실의 비누를 연상시키는 향입니다. 파우더리와 함께 사용될 때, 이불속에서 눈을 뜨고 아침을 맞이하는 듯한 따뜻하고, 포근한 느낌을 주는 향으로 많은 사람들이 '비누향'이라고 부르는 계열입니다. 깔끔하고 귀여운 이미지를 연상시킵니다.</small>
              </div>

              <img v-if="line == 'Fougere'" src="../assets/img/fougere.jpg" style="width:50%; height:12rem;">
              <p v-if="line == 'Fougere'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Fougere'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">싱싱하고 촉촉한 느낌의 향조로, 잎사귀를 연상시키는 프레시한 야성미에 라벤더의 지적인 따스함이 유능하고 도회적인 남성에게 어울리는 향입니다. 남성들에게는 포멀한 차림이나 신경을 써서 멋을 내고자 할 때 사용을 권하고 싶은 향기입니다.</small>
              </div>

              <img v-if="line == 'Fruity'" src="../assets/img/fruity.jpg" style="width:50%; height:12rem;">
              <p v-if="line == 'Fruity'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Fruity'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">무르익은 과일의 풍성하고 달콤한 느낌을 줍니다. 복숭아, 딸기, 바나나, 메론, 파인애플 등이 주로 사용되며 최근에는 향이 강한 열대과일도 사용되고 있습니다. 상큼하고 매력적인 과일향을 사용하여 달콤하고 귀여운 느낌을 줍니다.</small>
              </div>

              <img v-if="line == 'Gourmand'" src="../assets/img/gourmand.jpg" style="width:50%; height:12rem;">
              <p v-if="line == 'Gourmand'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Gourmand'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">프랑스어로 'Gourmand'은 미식가라는 뜻의 Groumand 계열은 잘 익은 과일이나, 벌꿀, 초콜릿 등 달콤한 향에 시나몬(계피향)이 더해진 스파이시한 향을 연상시킵니다. 달달한 향을 첨가하기 위해 마지막에 첨향하는 계열입니다.</small>
              </div>

              <img v-if="line == 'Green'" src="../assets/img/green.jpg" style="width:50%; height:12rem;">
              <p v-if="line == 'Green'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Green'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">초원을 연상시키는 싱그러운 풀이나 나뭇잎, 또는 나뭇가지를 연상시키는 젊고 신선한 상쾌한 향조로 친근감을 주는 것이 특징입니다. 신선한 풀에서 나는 풋내와 상쾌한 자연의 향으로 신선하고 깔끔한 느낌을 주기 위해 주로 탑노트에 사용합니다.</small>
              </div>

              <img v-if="line == 'Leather'" src="../assets/img/leather.jpg" style="width:50%; height:12rem;">
              <p v-if="line == 'Leather'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Leather'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">자작나무 타르와 가죽 향, 담배 향으로 남자 향수에 많이 사용됩니다. 환상적인 타르의 향이 동물적인 요소를 지녀 강한 개성을 느끼게 하는 향수입니다. 가죽 점퍼나, 새 차에서 맡을 수 있는 향으로 야생성을 느끼게 하는 향입니다.</small>
              </div>

              <img v-if="line == 'Musk'" src="../assets/img/musk.jpg" style="width:50%; height:12rem;">
              <p v-if="line == 'Musk'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Musk'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">사향 노루 생식선 부근의 사향샘에서 나는 아름다운 향입니다. 달콤하면서 파우더향이 나며, 포근한 향이나 따뜻한 느낌을 주는 매혹적인 향의 계열입니다. 지속력이 좋은 편이며, 잔향이 좋아 많은 사람들이 선호하는 대표적인 향입니다.</small>
              </div>

              <img v-if="line == 'Oriental'" src="../assets/img/oriental.png" style="width:50%; height:12rem;">
              <p v-if="line == 'Oriental'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Oriental'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">동양의 신비롭고 에로틱한 이미지를 표현한 향조입니다. 신비함과 우아함을 동물성 향료를 주조로 어우러져 무겁고 어두운 느낌을 줍니다. 여성의 우아함을 잘 표현하고, 열정적이며 이성에게 호소력이 강한 향입니다. 몽환적이며, 우아한 이미지를 연상시킵니다.</small>
              </div>

              <img v-if="line == 'Spicy'" src="../assets/img/spicy.jpg" style="width:50%; height:12rem;">
              <p v-if="line == 'Spicy'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Spicy'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">시나몬, 클로버, 후추, 생강과 같은 자극적인 향입니다. 강한 인상을 남길 수 있는 향이기 때문에 남성용 향수에서 많이 쓰이는 계열이며, 우디 계열의 향에 깊이를 더 해 줄 때도 사용되는 향입니다. 코 끝을 쏘는듯한 자극적인 향입니다.</small>
              </div>

              <img v-if="line == 'Vanilla'" src="../assets/img/vanilla.png" style="width:50%; height:12rem;">
              <p v-if="line == 'Vanilla'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Vanilla'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">향신료의 어머니라고 표현되는 바닐라(vanilla)는 향신료 중 하나로, 난초의 일종인 바닐라속에 속해 있으며, 세상에서 가장 고급스러운 단맛을 느끼게 해주는 향입니다. 꽃이 가득한 정원으로 걸으며 은은하게 풍기는 향의 계열입니다.</small>
              </div>

              <img v-if="line == 'Woody'" src="../assets/img/woody.png" style="width:50%; height:12rem;">
              <p v-if="line == 'Woody'" class="mt-3" style="font-weight:bold; font-size:1.2rem;">{{line}}</p>
              <div v-if="line == 'Woody'" style="width:50%; white-space:pre-line;">
                <small style="text-align:justify;">나무가 전하는 신선함과 중후함을 느낄 수 있는 무겁고 따뜻한 향기로 잔향이 무겁게 내려 앉아 고상하고 안정된 느낌을 선사합니다. 따뜻하고 부드러운 분위기로 중성적인 매력을 잔잔하게 전달할 수 있습니다. 서정적인 분위기를 연출하는 계열입니다.</small>
              </div>
            </div>
          </div>
          <!-- perfume 원료 -->
          <div class="mt-5">
            <span style="font-family: 'Black Han Sans', sans-serif; font-size:1.5rem">PERFUME NOTE</span>
            <div style="width:15rem; background-color:red">
              <small style="visibility:hidden">d</small>
            </div>
          </div>
          <div class="row mt-3">
            <div class="col-12 col-sm-12 col-md-6 mt-2">
              <!-- TOP NOTE -->
              <p class="mt-5 mb-0" style="font-weight:bold; font-size:1.2rem; color:DeepPink; white-space:nowrap;">TOP NOTE ---------------------------------------------</p>
              <small v-if="perfume.topList == false">해당 향수의 TOP NOTE는 존재하지 않습니다.</small>
              <small v-else v-for="top in perfume.topList" :key="top.id" style="font-weight:bold;">{{top}} </small>
              <p class="mt-5 mb-0" style="font-weight:bold; font-size:1.2rem; color:LightCoral; white-space:nowrap;">MIDDLE NOTE ----------------------------------------</p>
              <small v-if="perfume.midList == false">해당 향수의 MIDDLE NOTE는 존재하지 않습니다.</small>
              <small v-else v-for="mid in perfume.midList" :key="mid.id" style="font-weight:bold;">{{mid}} </small>
              <p class="mt-5 mb-0" style="font-weight:bold; font-size:1.2rem; color:LightPink; white-space:nowrap;">BASE NOTE -------------------------------------------</p>
              <small v-if="perfume.baseList == false">해당 향수의 TOP NOTE는 존재하지 않습니다.</small>
              <small v-else v-for="base in perfume.baseList" :key="base.id" style="font-weight:bold;">{{base}} </small>
            </div>
            <div class="col-12 col-sm-12 col-md-6 note" style="width:100%; height:25rem">
              
            </div>
          </div>


        </div>
        

      </div>
  </div>
</template>

<script>
import axios from 'axios'
import constants from '../lib/constants'
export default {
  data() {
    return {
      perfume:[],
    }
  },
  methods: {
    fetchPerfume() {
      axios.get(`${constants.SERVER_URL}/api/perfumes/perfume/${this.$route.params.id}/`)
        .then((res) => {
          this.perfume = res.data[0]
        }).catch((err) => {
          console.log(err.res.data)
        })
    },
    Adjective() {
      // var ad_count = new Array(45)
      // var Citrus = ['a','b','c','d']
      // var len = Citrus.length
      // for (var i; i<this.perfume.lineList.length; i++) {
      //   console.log(i)
      // }
      // for (var i; i < len; i++) {
      //   console.log(Citrus[i])
      // }

    },
  },
  created() {
    this.fetchPerfume()
    // this.Adjective()
    scrollTo(0,0)
  },
}
</script>

<style>
.note {
  background-image: url('../assets/img/note.jpg');
  background-repeat:no-repeat;
}
</style>