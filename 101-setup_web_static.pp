# Task #0 but by using Puppet

exec {'exec_1':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  path     => ['/usr/bin', '/bin'],
  provider => shell,
  returns  => [0,1]
}

exec {'exec_2':
  require  => Exec['exec_1'],
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  path     => ['/usr/bin', '/bin'],
  provider => shell,
}

exec {'exec_3':
  require  => Exec['exec_2'],
  command  => 'sudo mkdir -p /data/web_static/shared/',
  path     => ['/usr/bin', '/bin'],
  provider => shell,
}


exec {'exec_4':
  require  => Exec['exec_3'],
  command  => 'echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html',
  path     => ['/usr/bin', '/bin'],
  provider => shell,
}

exec {'exec_5':
  require  => Exec['exec_4'],
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  path     => ['/usr/bin', '/bin'],
  provider => shell,
}

exec { 'exec_6':
  require  => Exec['exec_5'],
  command  => 'sudo sed -i "s/server_name _;/server_name _;\n\tlocation \/hbnb_static\/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}/" /etc/nginx/sites-enabled/default',
  path     => ['/usr/bin', '/bin'],
  provider => shell,
  returns  => [0,1]
}

exec {'exec_7':
  require  => Exec['exec_6'],
  command  => 'sudo service nginx start',
  path     => ['/usr/bin', '/bin', '/usr/sbin'],
  provider => shell,
  returns  => [0,1]
}

exec {'exec_8':
  require  => Exec['exec_7'],
  command  => 'chown -R ubuntu:ubuntu /data/',
  path     => ['/usr/bin', '/bin'],
  provider => shell,
  returns  => [0,1]
}
