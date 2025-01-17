mkdir -p cardtext-fin
for i in $(ls cardtext/) ; do
    s3cmd put -m 'text/plain; charset=utf-8' cardtext/$i s3://mistivia-oss/ygo-card-text/$i
    mv cardtext/$i cardtext-fin/$i
done
