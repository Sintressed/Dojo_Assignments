
function rangeprint(start,end,ski)
{
    //while(start < end);
    for(var i = start; i < end; i = i + ski)
    {
        console.log(i);
        //start = start + ski;
    }
}
rangeprint(2,10,2);