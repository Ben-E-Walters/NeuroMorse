

# NeuroMorse
Repository for the code generation of the NeuroMorse Dataset, available at  https://doi.org/10.5281/zenodo.12702379. Here, Morse code has been converted into two channel spike trains. The training set consists of the top 50 words used in the English language converted into Morse spike sequences. The goal is to identify these keywords in the test set, which is a corpus of ~50,000 wikipedia articles converted into Morse spike sequences. For increased complexity, versions of the training and testing dataset exist with Jitter, Dropout and Poissonian noise added. More information can be found in our paper titled: "NEUROMORSE: A TEMPORALLY STRUCTURED DATASET FOR NEUROMORPHIC COMPUTING". Note: due to the large file sizes, the final generated dataset is only available at zenodo.

# Data Availability
Due to the large file sizes of the test set, the hdf5 data is available at DOI:10.5281/zenodo.12702379.

# Requirements
All scripts presented in this repository were created using python. Conda was used to manage the software environment, and all requirements can be found in the spec-file.txt file.

# Data Storage Scheme
The Data is stored in hdf5 format. For both the training and testing sets, there are 27 seperate files. The 'Clean' files are the original datasets with no noise added. The remaining files contain various types and levels of noise. The types of noise can be seen below, and explanations for the levels of noise can be seen in PAPER DOI.

![NoiseTypes](https://github.com/user-attachments/assets/7997c699-816f-44eb-8830-39191316c2c4)


<svg
   width="246.65456mm"
   height="162.42403mm"
   viewBox="0 0 246.65456 162.42403"
   version="1.1"
   id="svg5920"
   inkscape:version="1.1 (c68e22c387, 2021-05-23)"
   sodipodi:docname="NoiseTypes.svg"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <defs
     id="defs5917" />
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(8.439662,-27.575981)">
    <path
       style="fill:none;stroke:#000000;stroke-width:0.1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:0.8, 0.8;stroke-dashoffset:0;stroke-opacity:0.462151"
       d="M 61.585159,64.410888 V 185"
       id="path21780"
       sodipodi:nodetypes="cc" />
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.264583"
       x="31.302683"
       y="40.794609"
       id="text8711"><tspan
         sodipodi:role="line"
         id="tspan8709"
         style="stroke-width:0.264583"
         x="31.302683"
         y="40.794609">Clean</tspan></text>
    <g
       id="g21729">
      <path
         style="fill:none;stroke:#000000;stroke-width:1.13383;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M -3.4396618,90.257135 H 96.560337"
         id="path9451"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:none;stroke:#000000;stroke-width:1.12484;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M -3.4396618,64.81986 H 96.560337"
         id="path9453"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 7.2376808,89.810965 V 74.17938"
         id="path43026"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 31.513571,64.41134 V 48.77976"
         id="path43026-3"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 41.537161,64.4109 V 48.77931"
         id="path43026-4"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 51.561161,64.41089 V 48.77931"
         id="path43026-0"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 61.585161,64.41089 V 48.77931"
         id="path43026-39"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 84.573511,89.810895 V 74.17931"
         id="path43026-9"
         sodipodi:nodetypes="cc" />
    </g>
    <g
       id="g26605"
       transform="translate(-56.808783)">
      <path
         style="fill:none;stroke:#000000;stroke-width:1.13383;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="m 190.02367,97.119775 h 100"
         id="path9451-2"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:none;stroke:#000000;stroke-width:1.12484;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="m 190.02367,71.6825 h 100"
         id="path9453-8"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 202.25116,96.673605 V 81.04202"
         id="path43026-93"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 226.52705,71.27398 V 55.6424"
         id="path43026-3-3"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:0.187251"
         d="M 236.55064,71.27354 V 55.64195"
         id="path43026-4-3"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 246.57464,71.27353 V 55.64195"
         id="path43026-0-9"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 256.59864,71.27353 V 55.64195"
         id="path43026-39-2"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:0.188235"
         d="M 279.58699,96.673535 V 81.04195"
         id="path43026-9-7"
         sodipodi:nodetypes="cc" />
    </g>
    <g
       id="g26579">
      <path
         style="fill:none;stroke:#000000;stroke-width:1.13383;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="m -3.439662,179.66213 h 100"
         id="path9451-8"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:none;stroke:#000000;stroke-width:1.12484;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="m -3.439662,154.22486 h 100"
         id="path9453-9"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 10.809749,179.21596 V 163.58438"
         id="path43026-43"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 24.436829,153.81634 V 138.18476"
         id="path43026-3-6"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 38.234681,153.8159 V 138.18431"
         id="path43026-4-9"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 54.459254,153.81589 V 138.18431"
         id="path43026-0-4"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 61.58516,153.81589 V 138.18431"
         id="path43026-39-3"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 90.302301,179.21589 V 163.58431"
         id="path43026-9-9"
         sodipodi:nodetypes="cc" />
    </g>
    <g
       id="g26595"
       transform="translate(-27.228603,-62.544911)">
      <path
         style="fill:none;stroke:#000000;stroke-width:1.13383;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="m 160.44349,242.56971 h 100"
         id="path9451-5"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:none;stroke:#000000;stroke-width:1.12484;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="m 160.44349,217.13244 h 100"
         id="path9453-5"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 172.13177,242.12354 V 226.49196"
         id="path43026-8"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 196.40766,216.72392 V 201.09234"
         id="path43026-3-0"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#5487ff;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 175.95058,216.72358 V 201.092"
         id="path43026-3-0-2"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#5487ff;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 201.74858,216.72358 V 201.092"
         id="path43026-3-0-2-9"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#5487ff;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 252.61847,216.72358 V 201.092"
         id="path43026-3-0-2-3"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#5487ff;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 166.17794,242.28947 V 226.65789"
         id="path43026-3-0-2-5"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#5487ff;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 195.07622,242.28947 V 226.65789"
         id="path43026-3-0-2-9-3"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#5487ff;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 239.88034,242.28947 V 226.65789"
         id="path43026-3-0-2-3-6"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 206.43125,216.72348 V 201.09189"
         id="path43026-4-8"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 216.45525,216.72347 V 201.09189"
         id="path43026-0-5"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 226.47925,216.72347 V 201.09189"
         id="path43026-39-1"
         sodipodi:nodetypes="cc" />
      <path
         style="fill:#000000;fill-opacity:1;stroke:#ff5454;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         d="M 249.4676,242.12347 V 226.49189"
         id="path43026-9-8"
         sodipodi:nodetypes="cc" />
    </g>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.264583"
       x="160.93199"
       y="40.656807"
       id="text17273"><tspan
         sodipodi:role="line"
         id="tspan17271"
         style="stroke-width:0.264583"
         x="160.93199"
         y="40.656807">Dropout</tspan></text>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.264583"
       x="32.589771"
       y="126.89351"
       id="text18057"><tspan
         sodipodi:role="line"
         id="tspan18055"
         style="stroke-width:0.264583"
         x="32.589771"
         y="126.89351">Jitter</tspan></text>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:11.2889px;line-height:1.25;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.264583"
       x="153.0744"
       y="126.89351"
       id="text18721"><tspan
         sodipodi:role="line"
         id="tspan18719"
         style="stroke-width:0.264583"
         x="153.0744"
         y="126.89351">Poissonian</tspan></text>
    <path
       style="fill:none;stroke:#000000;stroke-width:0.1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:0.8, 0.8;stroke-dashoffset:0;stroke-opacity:0.462151"
       d="M 7.2376807,89.810965 V 185"
       id="path21772"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:0.8, 0.8;stroke-dashoffset:0;stroke-opacity:0.462151"
       d="M 31.513571,64.411338 V 185"
       id="path21774"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:0.8, 0.8;stroke-dashoffset:0;stroke-opacity:0.462151"
       d="M 41.537159,64.410899 V 185"
       id="path21776"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:0.8, 0.8;stroke-dashoffset:0;stroke-opacity:0.462151"
       d="M 51.561161,64.410888 V 185"
       id="path21778"
       sodipodi:nodetypes="cc" />
    <path
       style="fill:none;stroke:#000000;stroke-width:0.1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:0.8, 0.8;stroke-dashoffset:0;stroke-opacity:0.462151"
       d="M 84.573511,89.810893 V 185"
       id="path21782"
       sodipodi:nodetypes="cc" />
  </g>
</svg>

# Dataset Generation
This folder contains the files used to generate both the clean and noisy versions of the datasets, whilst the DatasetConversion.py file converts from the pckl format to hdf5.

# Linear Classifier
This folder contains the linear classifier test performed on the training set

# STDP Classifier
This folder contains the scripts used to run the STDP trained networks.

# Supervised Network
This folder contains a python notebook for a supervised learning approach for our dataset.

