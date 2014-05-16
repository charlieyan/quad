cd /sys/devices/bone_capemgr.*
cat slots
echo bone_pwm_P8_13 > slots
echo bone_pwm_P9_16 > slots
echo bone_pwm_P9_21 > slots
echo bone_pwm_P9_42 > slots
cat slots

cat "need to export items"
cat < /sys/kernel/debug/pwm
