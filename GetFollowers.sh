
if [  -z $1 ]
then
    username="basadaplanta";
else
    username=$1;
fi

echo "Getting followers list (this may take a while)";
twint -u $username --followers -o followers.txt
echo "Got followers list";

echo "Getting list of people followed (this may take a while)";
twint -u $username --following -o following.txt
echo "Got list of people following";