DROP TABLE IF EXISTS video;
DROP TABLE IF EXISTS article;
DROP TABLE IF EXISTS news;

CREATE TABLE video (
    uuid uuid NOT NULL,
    status integer,
    video_id text,
    url text,
    site text,
    title text,
    description text,
    thumbnail_url text,
    timestamp_creation timestamp with time zone,
    timestamp_publish timestamp with time zone,
    description_snippet text
);
CREATE UNIQUE INDEX index_video_uuid ON video (uuid);
CREATE UNIQUE INDEX index_video_id ON video (video_id);


CREATE TABLE article (
    uuid uuid NOT NULL,
    status integer,
    article_id text,
    timestamp_creation timestamp with time zone,
    timestamp_publish timestamp with time zone,
    title text,
    article_type text,
    site text,
    lang text,
    excerpt text,
    article_category text,
    url text,
    image_url text,
    body text,
    body_markdown text,
    CONSTRAINT title_article_type UNIQUE (title, article_type) -- No duplicates with the same title and article type
);
CREATE UNIQUE INDEX index_article_uuid ON article (uuid);
CREATE UNIQUE INDEX index_article_id ON article (article_id);


CREATE TABLE news (
    uuid uuid NOT NULL,
    status integer,
    news_id text,
    timestamp_creation timestamp with time zone,
    timestamp_publish timestamp with time zone,
    title text,
    news_type text,
    site text,
    lang text,
    excerpt text,
    news_category text,
    url text,
    image_url text,
    body text,
    body_markdown text
);
CREATE UNIQUE INDEX index_news_uuid ON news (uuid);
CREATE UNIQUE INDEX index_news_id ON news (news_id);
