import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

declare const module: any;

// создается web-сервер, в который весь код разработчика
// подключается в виде модулей
async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);

  // hotreload
  if (module.hot) {
    module.hot.accept();
    module.hot.dispose(() => app.close());
  }
}
bootstrap();
