<template>
    <div>
      <h1>&nbsp;Bank Map&nbsp;</h1>
      <div id="selectContainer" >
        <select 
        v-model="select1"
        style="height: 30px;font-size:17px;">
            <option  value="" selected>지역</option>
            <option v-for="c in centers" :value="c.position">{{ c.position }}</option>
        </select>
        <select 
        v-model="select2"
        style="height: 30px;font-size:17px;">
            <option value="" selected>지역</option>
            div
            <option v-for="c in centersDetail" :value="c.name">{{ c.name }}</option>
        </select>
      </div>
      <div id="mapContainer" ref="mapContainer" style="width: 90%; height: 70vh"></div>
      <div id="map" style="width:100%;height:100%;position:relative;overflow:hidden;"></div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, watch } from 'vue'
import { useMapStore } from '@/stores/map';
const mapStore = useMapStore()
  const { VITE_KAKAO_MAP_KEY } = import.meta.env
  
  const select1 = ref('')
  const select2 = ref('')
  const centers = mapStore.centers
  const centersDetail = ref([])

  
  const mapContainer = ref(null)
  
  onMounted(() => {
    loadKakaoMap(mapContainer.value)
  })
  const lat = ref(35.205439)
  const lng = ref(126.811537)
  const level = ref(3)
  
  watch(select1, (newValue) => {
    const idx = centers.findIndex(c => c.position == newValue)
    if (idx === -1) {
      lat.value = 35.205439
      lng.value = 126.811537
      level.value = 3
    } else {
      centersDetail.value = centers[idx].positionDetail
      lat.value = centers[idx].lat
      lng.value = centers[idx].lng
      level.value = centers[idx].level
    }
    loadKakaoMap(mapContainer.value)
  })
  watch(select2, (newValue) => {
    const idx = centersDetail.value.findIndex(c => c.name == newValue)
    if (idx === -1) {
      lat.value = 35.205439
      lng.value = 126.811537
      level.value = 3
    } else {
      lat.value = centersDetail.value[idx].lat
      lng.value = centersDetail.value[idx].lng
      level.value = centersDetail.value[idx].level
    }
    loadKakaoMap(mapContainer.value)
  })
  
  const loadKakaoMap = (mapContainer) => {
    const script = document.createElement('script')
    
    // script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${VITE_KAKAO_MAP_KEY}&autoload=false`
    //dapi.kakao.com/v2/maps/sdk.js?appkey=발급받은 APP KEY를 사용하세요&libraries=services"
    script.src = 'https://dapi.kakao.com/v2/maps/sdk.js?appkey=e04c544fccbbeb6f25e99a228ee891be&autoload=false&libraries=services'
    document.head.appendChild(script)
  
  
  
    script.onload = () => {
      window.kakao.maps.load(() => {
        var infowindow = new window.kakao.maps.InfoWindow({zIndex:1});
  
        const mapOption = {
          center: new window.kakao.maps.LatLng(lat.value, lng.value),
          level: level.value
        }
  
  
        var map = new window.kakao.maps.Map(mapContainer, mapOption); 
  
        // 장소 검색 객체를 생성합니다
        var ps = new window.kakao.maps.services.Places(map); 
  
        // 카테고리로 은행을 검색합니다
        ps.categorySearch('BK9', placesSearchCB, {useMapBounds:true}); 
  
        kakao.maps.event.addListener(map, 'dragend', function() {        
      
            var latlng = map.getCenter(); 
            lat.value = latlng.getLat()
            lng.value = latlng.getLng()
            ps.categorySearch('BK9', placesSearchCB, {useMapBounds:true}); 
  
        });
        kakao.maps.event.addListener(map, 'zoom_changed', function() {        
      
            level.value = map.getLevel();
            ps.categorySearch('BK9', placesSearchCB, {useMapBounds:true}); 
  
        });
  
  
        // 키워드 검색 완료 시 호출되는 콜백함수 입니다
        function placesSearchCB (data, status, pagination) {
            if (status === window.kakao.maps.services.Status.OK) {
                for (var i=0; i<data.length; i++) {
                    displayMarker(data[i]);    
                }
            }
        }
  
        
        function displayMarker(place) {
            // 마커를 생성하고 지도에 표시합니다
            var marker = new window.kakao.maps.Marker({
                map: map,
                position: new window.kakao.maps.LatLng(place.y, place.x) 
            });
            window.kakao.maps.event.addListener(marker, 'mouseover', function() {
                var ln = Math.max(Math.max(place.place_name.length, place.road_address_name.length), place.address_name.length)
                console.log(ln)
                infowindow.setContent('<div class="overlay_info" style="width:'+ ln * 13+'px">'
                  + '<div style="padding:5px;font-size:15px;">' + place.place_name  + '</div>'
                  + '<div style="padding:5px;font-size:12px;">' + place.road_address_name + '</div>'
                  + '<div style="padding:5px;font-size:10px;">' + place.address_name + '</div>'
                  + '</div>'
                );
                infowindow.open(map, marker);
            });
            window.kakao.maps.event.addListener(marker, 'mouseout', function() {
                // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
                infowindow.close();
                infowindow.open(map, marker);
            });
  
        }
  
  
  
      })
    }
  }
  </script>
  
  
  <style scoped>
  * {
    margin: 0 auto;
  }
  select {
    margin-right: 5px;
    border-radius: 5px;
    background-color: rgb(246, 244, 235); 
    width: 130px;
    border: 1.5px solid rgb(0, 55, 104);

  }
  #selectContainer {
    margin-left: 5% !important;
    margin: 1.5rem;
  }
h1 {
  color: rgb(0, 55, 104);  
  text-align: center;
  text-decoration: underline;
  text-underline-offset: 10px;
}
  #mapContainer {
    border-radius: 5px;

    border: 1.5px solid rgb(0, 55, 104);
  }
  </style>
  