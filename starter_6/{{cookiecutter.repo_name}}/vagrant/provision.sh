#-------------------------------------------------------------
# CONFIGS
#-------------------------------------------------------------

repo_name="{{ cookiecutter.repo_name }}"
project_name="{{ cookiecutter.project_name }}"
repo_dir="{{cookiecutter.repo_root_path}}"
project_dir="{{ cookiecutter.project_root_path }}"
django_reqs="{{ cookiecutter.django_reqs_path }}"
virtualenv_dir="{{ cookiecutter.virtualenv_dir_path }}"
log_color="\e[1;36m"


#-------------------------------------------------------------
# UTILITIES
#-------------------------------------------------------------


#    SUMMARY:  Logging Utility
#    EXAMPLE:  logit "This is a console log"
#    PARAMETERS:
#       MSG - enter a string that you want logit to log
logit () {
    echo -e "${log_color} $1"
}


#-------------------------------------------------------------
# INSTALL SOFTWARE
#-------------------------------------------------------------

# INFO: update ubuntu
logit "Updating Ubuntu"
sudo apt-get update

# INFO: install pip
logit "Updating installing pip"
sudo apt-get install -y python-pip

# INFO: install virtualenvwrapper
logit "Installing virtualenvwrapper"
sudo pip install virtualenvwrapper

#-------------------------------------------------------------
# CONFIGURE VIRTUALENVWRAPPER
#-------------------------------------------------------------

# INFO: configuring .profile
logit "configuring .profile"
sed -i '10i # virtualenvwrapper configuration' /home/vagrant/.profile
sed -i '11i export WORKON_HOME=/home/vagrant/.virtualenvs' /home/vagrant/.profile
sed -i '12i source /usr/local/bin/virtualenvwrapper.sh' /home/vagrant/.profile

# INFO: relaod .profile
logit "Reloading .profile"
source /home/vagrant/.profile

#-------------------------------------------------------------
# SETUP DJANGO
#-------------------------------------------------------------

# INFO: initialize virtualenvironment
logit "Creating ${repo_name} virtual environment..."
mkvirtualenv -r ${django_reqs} ${repo_name}

# INFO: activate virtualenv
logit "Activate virtual environment"
source ${virtualenv_dir}/${repo_name}/bin/activate

# INFO: move into django project
logit "Changing ${repo_name} folder"
cd ${repo_name}

# INFO: log user into virtualenv when they ssh into VM
logit "Configuring .bashrc"
cat << EOF >> /home/vagrant/.bashrc
    # login to virtualenv
    source ${virtualenv_dir}/${repo_name}/bin/activate
    # project directory
    cd ${repo_dir}
EOF

# INFO: move into django project
logit "Changing to ${repo_name} directory"
cd ${repo_dir}

# INFO: build initial Django DB tables
logit "Migrating Django DB"
python manage.py migrate

