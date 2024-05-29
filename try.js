async function get(sheetName){
   try {
     res = await fetch(`https://script.google.com/macros/s/AKfycbzjGuU3odON70nwq4KvYMHcU66GluccPDscjbKk17DzkAEYwS03WxXYPSm1y49LKEz5/exec?path=${sheetName}&action=read`)

     res = await res.json()

     console.log(res)
   } catch (error) {
    console.log(error)
   }
}

get('Impact_story')