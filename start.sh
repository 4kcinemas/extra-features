if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/4kcinemas/Naruto.git /Naruto
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Naruto
fi
cd /Naruto
pip3 install -U -r requirements.txt
echo "Starting 𝙽𝚊𝚛𝚞𝚝𝚘....🔥"
python3 bot.py
