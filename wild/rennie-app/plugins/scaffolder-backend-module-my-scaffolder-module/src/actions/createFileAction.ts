import { createTemplateAction } from '@backstage/plugin-scaffolder-node';
import fs from 'fs-extra';
import { resolveSafeChildPath } from '@backstage/backend-plugin-api';

export const createFileAction = () => {
  return createTemplateAction({
    id: 'my:custom:action',
    description: 'Creates a new file in the temporary workspace.',
    schema: {
      input: {
        type: 'object',
        required: ['filename', 'contents'],
        properties: {
          filename: {
            type: 'string',
            description: 'Name of the file to create.',
          },
          contents: {
            type: 'string',
            description: 'Contents of the file to write.',
          },
        },
      },
    },
    async handler(ctx) {
      const filePath = resolveSafeChildPath(ctx.workspacePath, ctx.input.filename);
      await fs.outputFile(filePath, ctx.input.contents);
      ctx.logger.info(`File ${ctx.input.filename} created at ${filePath}`);
    },
  });
};