#PS_VIEWER=ghostview

echo
echo Create spherical, layered-model, travel-time grids for NonLinLoc
cd taup
./TauP_Table_NLL.sh
echo
echo Visualize P travel-time grid
./plot_time.gmt.sh
${PS_VIEWER} ak135/ak135.P.DEFAULT.time.ps &
cd ..

echo
echo Run NonLinLoc
NLLoc run/neic_global.in

echo
echo Visualize each location in SeismicityViewer
java net.alomax.seismicity.Seismicity loc/global.19340115.*.grid0.loc.hyp
java net.alomax.seismicity.Seismicity loc/global.20031210.*.grid0.loc.hyp
java net.alomax.seismicity.Seismicity loc/global.20031214.*.grid0.loc.hyp
java net.alomax.seismicity.Seismicity loc/global.20040224.*.grid0.loc.hyp
java net.alomax.seismicity.Seismicity loc/global.20060717.*.grid0.loc.hyp
