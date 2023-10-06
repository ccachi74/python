import folium

# 위도
latitude = 37.394946
# 경도
longitude = 127.111104

m = folium.Map(location=[latitude, longitude],
               zoom_start=7, 
               width=750, 
               height=500
              )

folium.Marker([latitude, longitude],
              popup="판교역",
              tooltip="판교역 입구").add_to(m)

m.save('folium.html')