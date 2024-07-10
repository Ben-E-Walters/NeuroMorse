![RootTrees](https://github.com/jc427648/NeuroMorse/assets/30432434/680707f6-3ab2-4edc-bbfc-f1cab82e69e3)# NeuroMorse
Repository for the code generation of the NeuroMorse Dataset, available at 10.5281/zenodo.12702379. Note: due to the large file sizes, the final generated dataset is only available at zenodo.

# Data Storage Scheme
The Data is stored in hdf5 format. For both the training and testing sets, there are 27 seperate files. The 'Clean' files are the original datasets with no noise added. The remaining files contain various types and degrees of noise, as specified by their label. The directory tree for each file is as follows:

![Uplo<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   width="526.31824mm"
   height="432.36581mm"
   viewBox="0 0 526.31824 432.36581"
   version="1.1"
   id="svg26730"
   sodipodi:docname="RootTrees.svg"
   inkscape:version="1.1 (c68e22c387, 2021-05-23)"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <sodipodi:namedview
     id="namedview26732"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageshadow="2"
     inkscape:pageopacity="0.0"
     inkscape:pagecheckerboard="0"
     inkscape:document-units="mm"
     showgrid="false"
     fit-margin-left="5"
     fit-margin-top="5"
     fit-margin-right="5"
     fit-margin-bottom="5"
     inkscape:zoom="0.34698723"
     inkscape:cx="2135.5253"
     inkscape:cy="1551.9303"
     inkscape:window-width="3440"
     inkscape:window-height="1369"
     inkscape:window-x="-8"
     inkscape:window-y="-8"
     inkscape:window-maximized="1"
     inkscape:current-layer="layer1" />
  <defs
     id="defs26727" />
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(36.613565,1.7937613)">
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="12.962773"
       y="158.06528"
       id="text37813"><tspan
         sodipodi:role="line"
         id="tspan37811"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="12.962773"
         y="158.06528">Dropout-None Jitter-None Poisson-Low</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="287.77179"
       y="192.17371"
       id="text37813-1"><tspan
         sodipodi:role="line"
         id="tspan37811-8"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="287.77179"
         y="192.17371">Dropout-None Jitter-None Poisson-Low</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="12.962773"
       y="324.72012"
       id="text38333"><tspan
         sodipodi:role="line"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="12.962773"
         y="324.72012"
         id="tspan38335">Dropout-High Jitter-High Poisson-High</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="287.77179"
       y="311.33258"
       id="text38333-8"><tspan
         sodipodi:role="line"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="287.77179"
         y="311.33258"
         id="tspan38335-1">Dropout-High Jitter-High Poisson-High</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="39.843323"
       y="344.37595"
       id="text33027-7"><tspan
         sodipodi:role="line"
         id="tspan33025-3"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="39.843323"
         y="344.37595">Spikes</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="64.243828"
       y="364.11417"
       id="text33679-2"><tspan
         sodipodi:role="line"
         id="tspan33677-31"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="64.243828"
         y="364.11417">Times [ ]</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="64.243828"
       y="383.85236"
       id="text34175-1"><tspan
         sodipodi:role="line"
         id="tspan34173-6"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="64.243828"
         y="383.85236">Channels [ ]</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="39.843323"
       y="403.59055"
       id="text36027-8"><tspan
         sodipodi:role="line"
         id="tspan36025-15"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="39.843323"
         y="403.59055">Labels</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="64.243347"
       y="423.32861"
       id="text36027-7-3"><tspan
         sodipodi:role="line"
         id="tspan36025-6-0"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="64.243347"
         y="423.32861">Labels [ ]</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="39.304142"
       y="177.76927"
       id="text33027-1"><tspan
         sodipodi:role="line"
         id="tspan33025-01"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="39.304142"
         y="177.76927">Spikes</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="63.704651"
       y="197.50746"
       id="text33679-0"><tspan
         sodipodi:role="line"
         id="tspan33677-3"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="63.704651"
         y="197.50746">Times [ ]</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="63.704651"
       y="217.24565"
       id="text34175-7"><tspan
         sodipodi:role="line"
         id="tspan34173-2"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="63.704651"
         y="217.24565">Channels [ ]</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="39.304142"
       y="236.98387"
       id="text36027-0"><tspan
         sodipodi:role="line"
         id="tspan36025-1"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="39.304142"
         y="236.98387">Labels</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="63.70417"
       y="256.72189"
       id="text36027-7-1"><tspan
         sodipodi:role="line"
         id="tspan36025-6-4"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="63.70417"
         y="256.72189">Labels [ ]</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="6.1001296"
       y="13.34403"
       id="text27695"><tspan
         sodipodi:role="line"
         id="tspan27693"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="6.1001296"
         y="13.34403">root</tspan><tspan
         sodipodi:role="line"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="6.1001296"
         y="27.455156"
         id="tspan27697" /></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="12.962773"
       y="30.838779"
       id="text32429"><tspan
         sodipodi:role="line"
         id="tspan32427"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="12.962773"
         y="30.838779">Clean</tspan></text>
    <g
       id="g85755"
       transform="translate(71.710975,-21.02803)">
      <circle
         style="fill:#000000;stroke:#ff5454;stroke-width:0.1;stroke-dasharray:0.799999, 0.799999;stroke-opacity:0.188235"
         id="path57543"
         cx="15.730865"
         cy="292.75333"
         r="2.2875481" />
      <circle
         style="fill:#000000;stroke:#ff5454;stroke-width:0.1;stroke-dasharray:0.799999, 0.799999;stroke-opacity:0.188235"
         id="path57543-3"
         cx="15.730865"
         cy="307.99551"
         r="2.2875481" />
      <circle
         style="fill:#000000;stroke:#ff5454;stroke-width:0.1;stroke-dasharray:0.799999, 0.799999;stroke-opacity:0.188235"
         id="path57543-8"
         cx="15.730865"
         cy="323.2377"
         r="2.2875481" />
    </g>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="39.650829"
       y="50.576977"
       id="text33027"><tspan
         sodipodi:role="line"
         id="tspan33025"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="39.650829"
         y="50.576977">Spikes</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="64.051338"
       y="70.31517"
       id="text33679"><tspan
         sodipodi:role="line"
         id="tspan33677"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="64.051338"
         y="70.31517">Times [ ]</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="64.051338"
       y="90.053368"
       id="text34175"><tspan
         sodipodi:role="line"
         id="tspan34173"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="64.051338"
         y="90.053368">Channels [ ]</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="39.650829"
       y="109.79157"
       id="text36027"><tspan
         sodipodi:role="line"
         id="tspan36025"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="39.650829"
         y="109.79157">Labels</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="64.050858"
       y="129.52963"
       id="text36027-7"><tspan
         sodipodi:role="line"
         id="tspan36025-6"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="64.050858"
         y="129.52963">Labels [ ]</tspan></text>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:14.1111px;line-height:1.25;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.264583"
       x="-32.350815"
       y="13.479506"
       id="text60196"><tspan
         sodipodi:role="line"
         id="tspan60194"
         style="font-size:14.1111px;stroke-width:0.264583"
         x="-32.350815"
         y="13.479506">(a)</tspan></text>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:14.1111px;line-height:1.25;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.264583"
       x="232.92583"
       y="13.479506"
       id="text63146"><tspan
         sodipodi:role="line"
         id="tspan63144"
         style="font-size:14.1111px;stroke-width:0.264583"
         x="232.92583"
         y="13.479506">(b)</tspan></text>
    <g
       id="g57663-1"
       transform="translate(361.57004,40.176372)">
      <circle
         style="fill:#000000;stroke:#ff5454;stroke-width:0.1;stroke-dasharray:0.799999, 0.799999;stroke-opacity:0.188235"
         id="path57543-9"
         cx="8.7689505"
         cy="221.89217"
         r="2.2875481" />
      <circle
         style="fill:#000000;stroke:#ff5454;stroke-width:0.1;stroke-dasharray:0.799999, 0.799999;stroke-opacity:0.188235"
         id="path57543-3-1"
         cx="8.7689505"
         cy="237.13435"
         r="2.2875481" />
      <circle
         style="fill:#000000;stroke:#ff5454;stroke-width:0.1;stroke-dasharray:0.799999, 0.799999;stroke-opacity:0.188235"
         id="path57543-8-9"
         cx="8.7689505"
         cy="252.37654"
         r="2.2875481" />
    </g>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="280.90915"
       y="13.34403"
       id="text27695-0"><tspan
         sodipodi:role="line"
         id="tspan27693-1"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="280.90915"
         y="13.34403">root</tspan><tspan
         sodipodi:role="line"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="280.90915"
         y="27.455156"
         id="tspan27697-4" /></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="287.77179"
       y="30.838779"
       id="text32429-1"><tspan
         sodipodi:role="line"
         id="tspan32427-6"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="287.77179"
         y="30.838779">Clean</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="314.45984"
       y="50.576977"
       id="text33027-8"><tspan
         sodipodi:role="line"
         id="tspan33025-2"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="314.45984"
         y="50.576977">Spikes</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="338.86035"
       y="70.31517"
       id="text33679-7"><tspan
         sodipodi:role="line"
         id="tspan33677-4"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="338.86035"
         y="70.31517">Times [ ]</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="338.86035"
       y="90.053368"
       id="text34175-5"><tspan
         sodipodi:role="line"
         id="tspan34173-9"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="338.86035"
         y="90.053368">Channels [ ]</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="314.45984"
       y="210.24036"
       id="text33027-8-3"><tspan
         sodipodi:role="line"
         id="tspan33025-2-9"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="314.45984"
         y="210.24036">Spikes</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="338.86035"
       y="229.97855"
       id="text33679-7-9"><tspan
         sodipodi:role="line"
         id="tspan33677-4-5"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="338.86035"
         y="229.97855">Times [ ]</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="338.86035"
       y="249.71675"
       id="text34175-5-1"><tspan
         sodipodi:role="line"
         id="tspan34173-9-4"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="338.86035"
         y="249.71675">Channels [ ]</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="314.45984"
       y="333.17343"
       id="text33027-8-3-5"><tspan
         sodipodi:role="line"
         id="tspan33025-2-9-6"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="314.45984"
         y="333.17343">Spikes</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="338.86035"
       y="352.91162"
       id="text33679-7-9-8"><tspan
         sodipodi:role="line"
         id="tspan33677-4-5-9"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="338.86035"
         y="352.91162">Times [ ]</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
       x="338.86035"
       y="372.64981"
       id="text34175-5-1-5"><tspan
         sodipodi:role="line"
         id="tspan34173-9-4-8"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="338.86035"
         y="372.64981">Channels [ ]</tspan></text>
    <g
       id="g134825">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 4.9033139,21.93017 V 321.235"
         id="path132530"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 5.1729058,27.321973 H 12.991018"
         id="path132878" />
      <path
         style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 5.1729058,154.50112 H 12.991018"
         id="path132878-6" />
      <path
         style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 5.1729058,321.04043 H 12.991019"
         id="path132878-9" />
    </g>
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="M 278.7971,21.323602 V 307.08164"
       id="path132530-9"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 279.0667,26.715405 h 7.81811"
       id="path132878-33" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 279.0667,187.9977 h 7.81811"
       id="path132878-6-2" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 279.0667,306.81956 h 7.81811"
       id="path132878-9-2" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 54.642696,111.52275 v 15.0039"
       id="path132530-6-6"
       sodipodi:nodetypes="cc" />
    <g
       id="g135084">
      <path
         style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="m 31.439831,105.81632 h 7.818112"
         id="path132878-3-7" />
      <g
         id="g135028">
        <path
           style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           d="M 31.727534,32.848581 V 105.99321"
           id="path132530-1"
           sodipodi:nodetypes="cc" />
        <path
           style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           d="M 54.642696,52.259069 V 87.554298"
           id="path132530-6"
           sodipodi:nodetypes="cc" />
        <path
           style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           d="m 31.727534,46.597668 h 7.818112"
           id="path132878-3" />
        <path
           style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           d="m 54.642696,67.221313 h 7.818112"
           id="path132878-38" />
        <path
           style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           d="m 54.642696,87.305778 h 7.818112"
           id="path132878-381" />
      </g>
    </g>
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="M 305.64016,31.960394 V 45.953797"
       id="path132530-1-2"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="M 328.55533,51.370882 V 86.666111"
       id="path132530-6-7"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 305.64016,45.709481 h 7.81812"
       id="path132878-3-73" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 328.55533,66.333126 h 7.81811"
       id="path132878-38-5" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 328.55533,86.417591 h 7.81811"
       id="path132878-381-39" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 305.64016,197.16495 v 8.66168"
       id="path132530-1-2-1"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 328.55533,211.23783 v 35.29523"
       id="path132530-6-7-0"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 305.64016,205.57643 h 7.81812"
       id="path132878-3-73-6" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 328.55533,226.20007 h 7.81811"
       id="path132878-38-5-6" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 328.55533,246.28454 h 7.81811"
       id="path132878-381-39-4" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 305.35246,316.74027 v 11.30172"
       id="path132530-1-2-0"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 328.26763,333.45486 v 35.29523"
       id="path132530-6-7-5"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 305.35246,327.79346 h 7.81812"
       id="path132878-3-73-1" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 328.26763,348.4171 h 7.81811"
       id="path132878-38-5-5" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 328.26763,368.50157 h 7.81811"
       id="path132878-381-39-43" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 54.642696,126.27794 h 7.818112"
       id="path132878-381-3" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 31.727534,162.11864 v 70.24654"
       id="path132530-1-1"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 54.642696,178.63104 v 35.29523"
       id="path132530-6-8"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 54.642696,237.89472 v 15.0039"
       id="path132530-6-6-9"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 31.727534,172.96964 h 7.818112"
       id="path132878-3-2" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 54.642696,193.59328 h 7.818112"
       id="path132878-38-0" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 54.642696,213.67775 h 7.818112"
       id="path132878-381-9" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 54.642696,252.64991 h 7.818112"
       id="path132878-381-3-8" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 31.727534,328.32097 v 70.65092"
       id="path132530-1-1-2"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 54.642696,345.23775 v 35.29523"
       id="path132530-6-8-2"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 54.642696,404.50143 v 15.0039"
       id="path132530-6-6-9-2"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 31.727534,339.57635 h 7.818112"
       id="path132878-3-2-3" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 54.642696,360.19999 h 7.818112"
       id="path132878-38-0-2" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 54.642696,380.28446 h 7.818112"
       id="path132878-381-9-8" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       d="m 54.642696,419.25662 h 7.818112"
       id="path132878-381-3-8-0" />
    <g
       id="g136364"
       transform="translate(-26.286025)">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="314.45984"
         y="109.79156"
         id="text36027-2"><tspan
           sodipodi:role="line"
           id="tspan36025-3"
           style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
           x="314.45984"
           y="109.79156">Labels</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="338.85986"
         y="129.52962"
         id="text36027-7-4"><tspan
           sodipodi:role="line"
           id="tspan36025-6-6"
           style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
           x="338.85986"
           y="129.52962">Labels [ ]</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="338.85986"
         y="149.26793"
         id="text67325"><tspan
           sodipodi:role="line"
           id="tspan67323"
           style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
           x="338.85986"
           y="149.26793">Start Times [ ]</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
         x="338.85986"
         y="169.02594"
         id="text67857"><tspan
           sodipodi:role="line"
           id="tspan67855"
           style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:Arial;-inkscape-font-specification:Arial;stroke-width:0.264583"
           x="338.85986"
           y="169.02594">End Times [ ]</tspan></text>
      <path
         style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="m 305.35246,104.92813 h 7.81811"
         id="path132878-3-7-7" />
      <g
         id="g135834">
        <path
           style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           d="m 328.55533,111.66866 v 53.65819"
           id="path132530-6-7-6"
           sodipodi:nodetypes="cc" />
        <path
           style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           d="m 328.55533,125.54642 h 7.81811"
           id="path132878-38-5-3" />
        <path
           style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           d="m 328.55533,144.0545 h 7.81811"
           id="path132878-38-5-66" />
        <path
           style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           d="m 328.55533,165.08253 h 7.81811"
           id="path132878-38-5-52" />
      </g>
    </g>
  </g>
</svg>
ading RootTrees.svg…]()



# Linear Classifier
This file contains both the linear classifier tests performed on both the training and testing sets.

# Dataset Generation
This folder contains the files used to generate both the clean and noisy versions of the datasets, whilst the DatasetConversion.py file converts from the pckl format to hdf5.
