async function get(sheetName) {
  try {
    let res = await fetch(
      `https://script.google.com/macros/s/AKfycbzjGuU3odON70nwq4KvYMHcU66GluccPDscjbKk17DzkAEYwS03WxXYPSm1y49LKEz5/exec?path=${sheetName}&action=read`
    );

    const { data } = await res.json();

    console.log(data);
  } catch (error) {
    console.log(error);
  }
}

get("Impact_story");
