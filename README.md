This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.

## Connect to database using Python
To connect to database use the following code (You will need to plug in the correct address for the database_url (refer to discord))
```Python
import psycopg

database_url = "..."

conn = psycopg.connect(database_url)

# Example query
with conn.cursor() as cur:
    # Query to get table names and column details
    cur.execute("""
        SELECT table_name, column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = 'public'
        ORDER BY table_name, ordinal_position;
    """)
    schema = cur.fetchall()
    # Print schema details in a similar way to `.schema`
    current_table = None
    for table_name, column_name, data_type in schema:
        if table_name != current_table:
            print(f"\nTABLE:\n{table_name}\n")
            current_table = table_name
        print(f"    {column_name} {data_type}")

# Close the connection when done
conn.close()
```

## Sync local repository to match the master github repo (DELETES ALL UNPUSHED COMMITS)
Run these commands in your terminal if you need your local repository to match the master repository found on Github
These commands will delete any commits that have not been pushed. Make sure your commits are pushed before executing.
```Bash
git fetch origin
git reset --hard origin/master
```
