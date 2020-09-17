*********************************
Customizando o Amazon SageMaker
*********************************

Nessa etapa do workshop iremos utilizar frameworks de mercado e customizar nossas próprias imagens para
serem utilizadas com o Amazon SageMaker.

O Amazon SageMaker funciona da seguinte forma:

.. image:: _static/02-sagemaker-custom/sg_02.jpg

Com essa arquitetura podemos customizar o SageMaker para utilizar nossos próprios containers Docker.

Iremos criar uma instância gerenciada com o nosso ambiente de desenvolvimento Cloud9 já configurado com Docker. Para isso clique no botão abaixo:

.. image:: _static/cloudformation_launch_stack.png
   :target: https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=sagemaker-workshop&templateURL=https://aws-brasil-workshops.s3.amazonaws.com/workshop-amazon-sagemaker/container_cloudformation.yml
   :alt: Cloudformation launch Stack

Aguarde a criação do ambiente e siga os tópicos seguintes.

.. image:: _static/02-sagemaker-custom/sg_01.png

Utilizando frameworks com o Script Mode
------------------------------------------

Criando o seu próprio container
------------------------------------------

.. image:: _static/02-sagemaker-custom/sg_03.gif


Importando seu próprio modelo
------------------------------------------

Caso você já tenha um modelo treinado fora do Amazon SageMaker e queira utilizar, também é possível.
Nesse tópico iremos demonstrar como criar um endpoint de inferência utilizando um modelo de classificação
criado a partir do framework Tensorflow sem a utilização dos containers Script Mode.

Para prosseguir, no ambiente Jupyter já configurado vá para a pasta **labs/02-sagemaker-custom/byom-mode** e abra o notebook **sagemaker-custom-03.ipynb**.
Leia e execute cada passo do notebook.

.. image:: _static/02-sagemaker-custom/sg_04.png

**Obrigado pela participação no workshop! Agora você pode efetuar treinamentos e inferências em um ambiente escalável e com alta disponibilidade.**

.. important:: Iremos atualizar esse workshop com mais conteúdos. Então favorite e de uma estrela em nosso repositório =)
