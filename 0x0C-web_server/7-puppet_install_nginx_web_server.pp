# Install Nginx web server (w/ Puppet)

package {'nginx':
  ensure => 'present',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec {'301':
  command  => 'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com permanent;/" /etc/nginx/sites-enabled/default':
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
