# Author 
# 1. Kittipong Wongwipasamitkun
# 2. Nicole Tu
# 3. Sho Inagaki

FROM quay.io/jupyter/minimal-notebook:2023-11-19

RUN conda install -y python=3.11.6 \
    ipykernel=6.26.0 \
    matplotlib=3.8.2 \
    pandas=2.1.3 \
    scikit-learn=1.3.2 \
    requests=2.31.0 \
    ipython=8.17.2 \
    pytest=7.4.3 \
    click=8.1.7 \
    vl-convert-python=1.1.0 \
    seaborn=0.12.2 \
    jupyter-book=0.15.1 \
    vegafusion=1.4.5 \  
    vegafusion-python-embed=1.4.5 \  
    vegafusion-jupyter=1.4.5 \
    scipy=1.11.3 \
    myst-nb=0.17.2 \
    pip=23.1.2 \
    nb_conda_kernels=2.3.1 \
    numpy=1.25.2 \
    altair=5.1.2 \
    notebook=7.0.6 -c conda-forge
