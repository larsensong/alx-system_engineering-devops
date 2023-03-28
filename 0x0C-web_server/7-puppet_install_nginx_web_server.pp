# Script that installs and configures Nginx
exec {'update':
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'sudo apt-get -y update',
}

exec {'install':
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'sudo apt-get -y install nginx',
}

exec {'echo_html':
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'sudo echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html',
}

exec {'sed_config':
  command  => 'sudo sed -i "/server_name _;/ a\\\trewrite ^/redirect_me http://www.youtube.com permanent;" /etc/nginx/sites-available/default',
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
}

exec {'start':
  command  => 'sudo service nginx start',
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
}
