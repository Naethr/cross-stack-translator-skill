# Initial Stack Mappings

These mappings are starting points only. They are not exhaustive, and repository evidence should override them.

## Express + Prisma -> Laravel

- Express routes roughly map to Laravel route files such as `routes/web.php` or `routes/api.php`.
- Express controllers or route handlers roughly map to Laravel controllers under `app/Http/Controllers`.
- Prisma models roughly map to Eloquent models, but Eloquent models are active record objects while Prisma models are schema-backed client types.
- Prisma migrations roughly map to Laravel migrations, but Laravel migrations are PHP classes and often pair with Eloquent conventions.
- Express middleware roughly maps to Laravel middleware, though Laravel applies middleware through route groups, controllers, and kernel configuration.

## Express + Prisma -> Django

- Express routes roughly map to Django URL configuration files such as `urls.py`.
- Express route handlers roughly map to Django views.
- Prisma models roughly map to Django models, but Django models are active record style and are defined directly in Python code.
- Prisma migrations roughly map to Django migrations generated from model changes.
- Express middleware roughly maps to Django middleware, though Django middleware is usually configured globally in settings.

## Next.js -> Nuxt

- Next.js pages or app routes roughly map to Nuxt pages and file-based routing.
- Next.js layouts roughly map to Nuxt layouts, but lifecycle and data-fetching conventions differ.
- Next.js server components do not have a direct Nuxt equivalent.
- Next.js API routes roughly map to Nuxt server routes, but the runtime conventions differ.
- Next.js configuration roughly maps to `nuxt.config`, with framework-specific differences in modules and rendering options.

## Laravel -> NestJS

- Laravel controllers roughly map to NestJS controllers.
- Laravel services or action classes roughly map to NestJS providers, but NestJS uses explicit dependency injection as a core pattern.
- Laravel middleware roughly maps to NestJS middleware, guards, pipes, or interceptors depending on the concern.
- Eloquent models do not directly map to one NestJS concept; the equivalent depends on the chosen ORM.
- Laravel route files differ from NestJS decorator-based routing inside controller classes.
