#!/bin/bash
APP_USER=bayc
APP_HOME=/srv/bayc
SUDO_USER=bayc_super
SUDO_PASS=pass@1234


echo "--> Creating superuser '$SUDO_USER'"
useradd --user-group --no-create-home \
    --shell /bin/bash \
    $SUDO_USER
echo $SUDO_USER:$SUDO_PASS | chpasswd
adduser $SUDO_USER sudo
echo "$SUDO_USER ALL=(ALL) NOPASSWD:ALL" | tee /etc/sudoers.d/90-$SUDO_USER

echo "--> Creating application user '$APP_USER'"
mkdir -p $APP_HOME
useradd --system --user-group \
    --shell /bin/bash \
    --home-dir $APP_HOME \
    $APP_USER
chown $APP_USER: $APP_HOME

echo "--> Updating user '$SUDO_USER' and '$APP_USER' groups"
usermod -aG $APP_USER $SUDO_USER
usermod -aG $SUDO_USER $APP_USER