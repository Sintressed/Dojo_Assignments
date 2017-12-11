var HOUR = 12;
var MINUTE = 32;
var PERIOD = "PM";
var saying = ""
var morning = "in the morning";
var evening = "in the evening";
if (PERIOD == "AM")
{
     saying = morning;
}
else{
    saying = evening;
}
if(MINUTE < 30)
{
    console.log("its almost " + HOUR + " " + saying)
}
else{
        console.log("its almost " + (HOUR + 1) + " " + saying)
    }
