# Author 
# 1. Kittipong Wongwipasamitkun
# 2. Nicole Tu
# 3. Sho Inagaki

FROM quay.io/jupyter/minimal-notebook
COPY environment.yml /tmp/
RUN conda env create -f /tmp/environment.yml