//@version=4
study("Efficient Trend Step",overlay=true)
length = input(100),fast = input(50),slow = input(200)
//
src = close
er = abs(change(src,length))/sum(abs(change(src)),length)
dev = er*stdev(src*2,fast) + (1-er)*stdev(src*2,slow)
a = 0.
a := bar_index < 9 ? src : src > a[1] + dev ? src : src < a[1] - dev ? src : a[1]
//
css = fixnan(a > a[1] ? #2E9AFE : a < a[1] ? #e65100 : na)
plot(a,color=css,transp=0,linewidth = 3)