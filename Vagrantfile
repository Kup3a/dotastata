# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "testenv"
  # config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
  config.vm.box_url = "file://./data/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.network "private_network", ip: "192.168.0.4"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"
  # config.vm.synced_folder "data", "/home/vagrant"
  # ��������� ������� ��������� �����
  config.vm.synced_folder ".", "/vagrant", disabled: true
  # ������� ����� � �������� �� ����� � ������ ������� �� �����. ������� ��� �����, ����� ������ data, �� ������� ����� ������������� ��������� �����
  config.vm.synced_folder ".", "/home/vagrant/dotastata"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
  config.vm.provision "shell", inline: <<-SHELL
    # this folder is mounted as shared on guest; but on host this is folder with vagrantfile
    hh=/home/vagrant/dotastata
    cd $hh/data
    # i can install any python version
    sudo apt-get --yes update
    sudo apt-get --yes install postgresql-9.3
    # sudo apt-get --yes install python 3.5
    # python get-pip.py
    # pip install virtualenv
    # this is conda install. it's not very good but pohui
    pp=/home/vagrant/anaconda3
    # before "vagrant up" i should put conda-file in shared folder on host or i should add getting conda command here
    bash Anaconda3-4.2.0-Linux-x86_64.sh -b -p $pp
    echo export PATH=/home/vagrant/anaconda3/bin:$PATH >> /home/vagrant/.bashrc
    # this was need for handly installing extra packages
    sudo chown -R vagrant /home/vagrant/anaconda3/
    # making env with packages from file 
    $pp/bin/conda create --yes -p $pp/envs/env_dj python=3 --file $hh/requirements.txt	
    # creating db via script
    ./postgresql_up.sh
  SHELL
end
