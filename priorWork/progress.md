installing operating system
===========================
*    get host's ip address using angstrom or w/e
*    https://rcn-ee.net/deb/microsd/trusty/
*    use the 14.04 img.xz, boot from it
*    let it sit there for 45 min
*    follow this tutorial to expand to use entire uSD
*    http://elinux.org/Beagleboard:Expanding_File_System_Partition_On_A_microSD
*    at this point, you need to have:
*    default boot uSD, uSD 16 GB (or however big your uSD is)

setting up on os
================
*    ssh-keygen -t rsa
*    upload to github the key
*    clone the repository git@github.com:charlieyan/quad.git
*    set up python (setup/setup_python.sh)
*    install vim
*    set up dtc (setup/dtc.sh)
*    set up pwm (setup/setup_pwm.sh)
*    mv the .dtbo files to /lib/firmware
*    disable the hdmi by modifying uEnv.txt
*    mkdir /mnt/boot/
*    mount /dev/mmcblk0p1 /mnt/boot/
*    vim /mnt/boot/uEnv.txt
*    add "optargs=quiet capemgr.disable_partno=BB-BONELT-HDMI,BB-BONELT-HDMIN"
*    set up crontabs to control system LED on reboot
*    @reboot /home/ubuntu/quad/bootScript.sh
*    restart by shutdown -r now, then
*    cat /sys/devices/bone_capemgr.*    /slots and ls /dev/spi*    
*    make sure /dev/spi2.0 exists

finally
=======
*    run python rev.py