# Install Nginx web server (w/ Puppet)

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,

}

exec {'Hello':
  command  => 'sudo echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec {
  command  => 'sudo sed -i "s/s/server_name _;/server_name _;\n\trewrite ^\/redirect_me \
wrapped > https:\/\/www.youtube.com permanent;/" /etc/nginx/sites-enabled/default',
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
